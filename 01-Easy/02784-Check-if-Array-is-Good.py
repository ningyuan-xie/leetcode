"""2784. Check if Array is Good
Link: https://leetcode.com/problems/check-if-array-is-good/
Difficulty: Easy
Description: You are given an integer array nums. We consider an array good if it is a permutation of
an array base[n].
base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1
to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and
base[3] = [1, 2, 3, 3].
Return true if the given array is good, otherwise return false.
Note: A permutation of integers represents an arrangement of these numbers."""

from typing import List


class Solution:
    @staticmethod
    def isGood(nums: List[int]) -> bool:
        """Optimal Solution: Frequency Count. Time Complexity: O(n), Space Complexity: O(1)"""
        max_num = max(nums)
        count = [0] * (max_num + 1)

        # Count the number of occurrences of each number
        for num in nums:
            count[num] += 1

        # Check number from 1 to max_num - 1
        for i in range(1, max_num):
            if count[i] != 1:
                return False

        # Check the maximum number
        return count[max_num] == 2


# Unit Test: nums = [2, 1, 3], Output: false
assert Solution.isGood([2, 1, 3]) is False

# Unit Test: nums = [1, 3, 3, 2], Output: true
assert Solution.isGood([1, 3, 3, 2]) is True

# Unit Test: nums = [1, 1], Output: true
assert Solution.isGood([1, 1]) is True

# Unit Test: nums = [3, 4, 4, 1, 2, 1], Output: false
assert Solution.isGood([3, 4, 4, 1, 2, 1]) is False

print("All unit tests are passed")
