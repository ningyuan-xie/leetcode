"""3289. The Two Sneaky Numbers of Digitville
Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
Difficulty: Easy
Description: In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.
As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville."""

from typing import List


class Solution:
    @staticmethod
    def getSneakyNumbers(nums: List[int]) -> List[int]:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Create a dictionary to count the occurrences of each number
        count = {}
        
        # Count the occurrences of each number in nums
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Find the two numbers that appear twice
        sneaky_numbers = [num for num, cnt in count.items() if cnt == 2]
        
        return sneaky_numbers


# Unit Test: nums = [0,1,1,0], Output: [0, 1]
assert sorted(Solution.getSneakyNumbers([0, 1, 1, 0])) == [0, 1]

# Unit Test: nums = [0,3,2,1,3,2], Output: [2, 3]
assert sorted(Solution.getSneakyNumbers([0, 3, 2, 1, 3, 2])) == [2, 3]

# Unit Test: nums = [7,1,5,4,3,4,6,0,9,5,8,2], Output: [4, 5]
assert sorted(Solution.getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])) == [4, 5]

print("All unit tests are passed.")
