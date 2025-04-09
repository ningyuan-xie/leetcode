"""2206. Divide Array Into Equal Pairs
Link: https://leetcode.com/problems/divide-array-into-equal-pairs/
Difficulty: Easy
Description: You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:
- Each element belongs to exactly one pair.
- The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false."""

from typing import List


class Solution:
    @staticmethod
    def divideArray(nums: List[int]) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Count the occurrences of each number
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        # nums = [3,2,3,2,2,2] -> num_count = {3: 2, 2: 4}

        # Check if the array can be divided into equal pairs
        for count in num_count.values():
            if count % 2 != 0:
                return False
        return True


# Unit Test: nums = [3,2,3,2,2,2], Output: True
assert Solution.divideArray([3, 2, 3, 2, 2, 2]) is True

# Unit Test: nums = [1,2,3,4], Output: False
assert Solution.divideArray([1, 2, 3, 4]) is False

print("All unit tests are passed")
