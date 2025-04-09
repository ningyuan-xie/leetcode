"""1512. Number of Good Pairs
Link: https://leetcode.com/problems/number-of-good-pairs/
Difficulty: Easy
Description: Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j."""

from typing import List


class Solution:
    @staticmethod
    def numIdenticalPairs(nums: List[int]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the count of good pairs
        count = 0
        # Initialize the dictionary to store the frequency of each number
        freq = {}

        # Iterate through the array
        for num in nums:
            # Check if the number is in the dictionary
            if num in freq:
                # Increment the count of good pairs by the previous frequency
                count += freq[num]  # count = 1 + 2 + 3 + ... + n
                # Increment the previous frequency
                freq[num] += 1
            else:
                # Add the number to the dictionary
                freq[num] = 1

        return count


# Unit Test: nums = [1, 2, 3, 1, 1, 3], Output: 4
assert Solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4

# Unit Test: nums = [1, 1, 1, 1], Output: 6
assert Solution.numIdenticalPairs([1, 1, 1, 1]) == 6

# Unit Test: nums = [1, 2, 3], Output: 0
assert Solution.numIdenticalPairs([1, 2, 3]) == 0

# Unit Test: nums = [1, 1, 1, 1, 1], Output: 10
assert Solution.numIdenticalPairs([1, 1, 1, 1, 1]) == 10

print("All unit tests are passed.")
