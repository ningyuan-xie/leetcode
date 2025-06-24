"""2367. Number of Arithmetic Triplets
Link: https://leetcode.com/problems/number-of-arithmetic-triplets/
Difficulty: Easy
Description: You are given a 0-indexed, strictly increasing integer array nums and a positive integer
diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
- i < j < k,
- nums[j] - nums[i] == diff, and
- nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets."""

from typing import List


class Solution:
    @staticmethod
    def arithmeticTriplets(nums: List[int], diff: int) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # Create a set to store the elements in nums
        num_set = set(nums)
        count = 0

        for num in nums:
            if (num - diff in num_set) and (num - 2 * diff in num_set):
                count += 1

        return count


# Input: nums = [0,1,4,6,7,10], diff = 3, Output: 2
assert Solution.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) == 2

# Input: nums = [4,5,6,7,8,9], diff = 2, Output: 2
assert Solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) == 2

print("All unit tests are passed.")
