"""3300. Minimum Element After Replacement With Digit Sum
Link: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
Difficulty: Easy
Description: You are given an integer array nums.
You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements."""

from typing import List


class Solution:
    @staticmethod
    def minElement(nums: List[int]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the minimum element to the first element in nums
        min_element = nums[0]
        
        # Iterate through the array to find the minimum element
        for num in nums:
            # Replace the current element with the sum of its digits
            num = sum(int(digit) for digit in str(num))
            
            # Update the minimum element if the new element is smaller
            min_element = min(min_element, num)
            
        return min_element


# Input: nums = [10,12,13,14], Output: 1
assert Solution.minElement([10,12,13,14]) == 1

# Input: nums = [1,2,3,4], Output: 1
assert Solution.minElement([1,2,3,4]) == 1

# Input: nums = [999,19,199], Output: 10
assert Solution.minElement([999,19,199]) == 10

print("All unit tests are passed.")
