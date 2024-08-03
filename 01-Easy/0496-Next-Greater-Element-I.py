"""496. Next Greater Element I
Link: https://leetcode.com/problems/next-greater-element-i/
Difficulty: Easy
Description: The next greater element of some element x in an array
is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that
ans[i] is the next greater element as described above.
Follow up: Could you find an O(nums1.length + nums2.length) solution?"""

from typing import List


class Solution:
    @staticmethod
    def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        """Sub-Optimal Solution: Brute Force. Time Complexity: O(n^2), Space Complexity: O(n)
           The order of nums1 does not matter so no need to loop it; the order of nums2 matters"""
        # Initialize a hashmap for nums1. E.g. nums1 = [4, 1, 2]
        num1_index = {n: i for i, n in enumerate(nums1)}  # [4, 1, 2] -> {4: 0, 1: 1, 2: 2}
        result = [-1] * len(nums1)  # [-1, -1, -1]

        # Outer loop: iterate through every number in nums2 array
        for i in range(len(nums2)):  # E.g. nums2 = [1, 3, 4, 2]
            current_element = nums2[i]
            # Proceed only if the current number is also in nums1
            if current_element in num1_index:
                # Inner loop: iterate through the rest of the nums2 array
                for j in range(i + 1, len(nums2)):  # Skip when reaching nums2's final number
                    if nums2[j] > current_element:
                        # Next greater element found: nums2[1] = 3 > nums2[0] = 1
                        next_greater_element = nums2[j]
                        # Use hashmap to find the index of the current element in nums1
                        current_element_index = num1_index[current_element]
                        result[current_element_index] = next_greater_element
                        break
        # [-1, -1, -1] -> [-1, 3, -1]
        return result

    @staticmethod
    def nextGreaterElementStack(nums1: List[int], nums2: List[int]) -> List[int]:
        """Optimal Solution: Monotonic Stack. Time Complexity: O(n), Space Complexity: O(n)
           Monotonic Stack remembers the elements in descending order, allowing multiple comparisons"""
        # Initialize a hashmap for nums1. E.g. nums1 = [4, 1, 2]
        num1_index = {n: i for i, n in enumerate(nums1)}  # [4, 1, 2] -> {4: 0, 1: 1, 2: 2}
        result = [-1] * len(nums1)  # [-1, -1, -1]
        stack = []  # A stack to store the current element in decreasing order for comparison

        # Iterate through every number in nums2 array
        for i in range(len(nums2)):  # E.g. nums2 = [1, 3, 4, 2]
            current_element = nums2[i]

            # Because we have a decreasing stack, when we finally find the next greater element,
            # we can check and pop multiple elements from the stack instead of just one element
            while stack and current_element > stack[-1]:
                # Next greater element found
                previous_element = stack.pop()
                # Use hashmap to find the index of the previous element in nums1
                previous_element_index = num1_index[previous_element]
                result[previous_element_index] = current_element

            # Append the current element to stack only if:
            # 1. it < the previous element in stack (if non-empty), so stack is in decreasing order
            # 2. it is also in nums1
            if current_element in num1_index:
                # Stack stores the current element in decreasing order
                stack.append(current_element)
        return result


# Unit Test: Input: nums1 = [4,1,2], nums2 = [1,3,4,2], Output: [-1,3,-1]
assert Solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

# Unit Test: Input: nums1 = [2,4], nums2 = [1,2,3,4], Output: [3,-1]
assert Solution.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]

# Unit Test: Input: nums1 = [4,1,2], nums2 = [2,1,3,4], Output: [-1,3,3]
assert Solution.nextGreaterElementStack([4, 1, 2], [2, 1, 3, 4]) == [-1, 3, 3]

print("All unit tests are passed")
