"""496. Next Greater Element I
Link: https://leetcode.com/problems/next-greater-element-i/
Difficulty: Easy
Description: The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
Follow up: Could you find an O(nums1.length + nums2.length) solution?"""

from typing import List


class Solution:
    @staticmethod
    def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        """Optimal Solution: Hash Table & Monotonic Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        # Create a dictionary to store the next greater elements
        next_greater = {}
        monotonic_stack = []  # monotonic decreasing stack

        # Iterate through nums2 to find the next greater elements
        for num in nums2:
            # Pop elements from the stack when num > the top of the stack
            while monotonic_stack and monotonic_stack[-1] < num:
                next_greater[monotonic_stack.pop()] = num
            monotonic_stack.append(num)

        # Fill in -1 for elements that do not have a next greater element
        for num in monotonic_stack:
            next_greater[num] = -1

        # Map the results for nums1 using the next_greater dictionary
        return [next_greater[num] for num in nums1]


def unit_tests():
    # Input: nums1 = [4,1,2], nums2 = [1,3,4,2], Output: [-1,3,-1]
    assert Solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

    # Input: nums1 = [2,4], nums2 = [1,2,3,4], Output: [3,-1]
    assert Solution.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]

    # Input: nums1 = [4,1,2], nums2 = [2,1,3,4], Output: [-1,3,3]
    assert Solution.nextGreaterElement([4, 1, 2], [2, 1, 3, 4]) == [-1, 3, 3]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
