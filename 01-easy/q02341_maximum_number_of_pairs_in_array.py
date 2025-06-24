"""2341. Maximum Number of Pairs in Array
Link: https://leetcode.com/problems/maximum-number-of-pairs-in-array/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums. In one operation, you may do the following:
- Choose two integers in nums that are equal.
- Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.
Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are
formed and answer[1] is the number of leftover integers in nums after doing the operation as many
times as possible."""

from typing import List


class Solution:
    @staticmethod
    def numberOfPairs(nums: List[int]) -> List[int]:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Create a hash table to store the frequency of each number
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1  # E.g. [1, 3, 2, 1, 3, 2, 2] -> {1: 2, 3: 2, 2: 3}

        # Count the number of pairs and leftover integers
        pairs, leftover = 0, 0
        for (num, freq) in frequency.items():
            pairs += freq // 2
            leftover += freq % 2

        return [pairs, leftover]


# Input: nums = [1,3,2,1,3,2,2], Output: [3,1]
assert Solution.numberOfPairs([1, 3, 2, 1, 3, 2, 2]) == [3, 1]

# Input: nums = [1,1], Output: [1,0]
assert Solution.numberOfPairs([1, 1]) == [1, 0]

print("All unit tests are passed.")
