"""2815. Max Pair Sum in an Array
Link: https://leetcode.com/problems/max-pair-sum-in-an-array/
Difficulty: Easy
Description: You are given an integer array nums. You have to find the maximum sum of a pair of
numbers from nums such that the largest digit in both numbers is equal.
For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.
Return the maximum sum or -1 if no such pair exists."""

from typing import List


class Solution:
    @staticmethod
    def maxSum(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the maximum sum
        max_sum = -1

        def largest_digit(n: int) -> int:
            """Helper function to find the largest digit in a number"""
            return max([int(digit) for digit in str(n)])

        def sum_two_largest(l: List[int]) -> int:
            """Helper function to sum up the two largest numbers in a list"""
            first, second = float('-inf'), float('-inf')
            for number in l:
                if number > first:
                    second, first = first, number  # Update both first and second
                elif number > second:
                    second = number  # Update second
            return first + second

        # Create a dictionary to store the numbers with the same largest digit
        max_dict = {}
        for num in nums:
            largest = largest_digit(num)
            # .setdefault(largest, []) sets [] as the default value for the key largest
            # E.g. {2: [112], 3: [131], 4: [411]}; {6: [2536, 1613, 3366, 162]}
            max_dict.setdefault(largest, []).append(num)

        for key in max_dict:
            if len(max_dict[key]) > 1:
                # Find the two largest numbers in the list
                max_sum = max(max_sum, sum_two_largest(max_dict[key]))
        return max_sum


# Unit Test: nums = [112,131,411], Output: -1
assert Solution.maxSum([112, 131, 411]) == -1

# Unit Test: nums = [2536,1613,3366,162], Output: 5902
assert Solution.maxSum([2536, 1613, 3366, 162]) == 5902

# Unit Test: nums = [51,71,17,24,42], Output: 88
assert Solution.maxSum([51, 71, 17, 24, 42]) == 88

print("All unit tests are passed")
