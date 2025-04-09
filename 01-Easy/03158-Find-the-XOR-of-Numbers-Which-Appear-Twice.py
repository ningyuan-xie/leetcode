"""3158. Find the XOR of Numbers Which Appear Twice
Link: https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice
Difficulty: Easy
Description: You are given an array nums, where each number in the array appears either once
or twice.
Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number
appears twice."""

from typing import List


class Solution:
    @staticmethod
    def findXOR(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a dictionary to count occurrences of each number
        count = {}
        # Iterate through the array and count occurrences
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Initialize the result variable
        result = 0
        # Iterate through the dictionary and XOR numbers that appear twice
        for num, cnt in count.items():
            if cnt == 2:
                result ^= num

        # Return the final result
        return result


# Unit Test: nums = [1,2,1,3], Output = 1
assert Solution.findXOR([1, 2, 1, 3]) == 1

# Unit Test: nums = [1,2,3], Output = 0
assert Solution.findXOR([1, 2, 3]) == 0

# Unit Test: nums = [1,2,2,1], Output = 3
assert Solution.findXOR([1, 2, 2, 1]) == 3

print("All unit tests are passed")
