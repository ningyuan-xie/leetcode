"""2562. Find the Array Concatenation Value
Link: https://leetcode.com/problems/find-the-array-concatenation-value/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums.
The concatenation of two numbers is the number formed by concatenating their numerals.
- For example, the concatenation of 15, 49 is 1549.
The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:
- If there exists more than one number in nums, pick the first element and last element in nums
respectively and add the value of their concatenation to the concatenation value of nums, then
delete the first and last element from nums.
- If one element exists, add its value to the concatenation value of nums, then delete it.
Return the concatenation value of the nums."""

from typing import List


class Solution:
    @staticmethod
    def findTheArrayConcVal(nums: List[int]) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        left, right = 0, len(nums) - 1
        total = 0

        while left < right:
            # Concatenate nums[left] and nums[right] and add to total
            total += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1

        # If nums has odd length, add the middle element to total
        if left == right:
            total += nums[left]

        return total


# Unit Test: nums = [7,52,2,4], Output: 596
assert Solution.findTheArrayConcVal([7, 52, 2, 4]) == 596

# Unit Test: nums = [5,14,13,8,12], Output: 673
assert Solution.findTheArrayConcVal([5, 14, 13, 8, 12]) == 673

print("All unit tests are passed.")
