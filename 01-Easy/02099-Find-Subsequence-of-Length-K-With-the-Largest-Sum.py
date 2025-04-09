"""2099. Find Subsequence of Length K With the Largest Sum
Link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum
Difficulty: Easy
Description: You are given an integer array nums and an integer k. You want to find a subsequence of
nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements."""

from typing import List


class Solution:
    @staticmethod
    def maxSubsequenceSum(nums: List[int], k: int) -> List[int]:
        """Optimal Solution: Sorting by Value & Index. Time Complexity: O(n), Space Complexity: O(1)"""
        # Get the largest `k` elements with their indices
        # E.g. nums = [2, 1, 3, 3], k = 2 -> [(3, 2), (3, 3)]
        largest_k = sorted([(num, i)
                            for (i, num) in enumerate(nums)],
                           key=lambda x: x[0], reverse=True)[:k]

        # Sort these `k` elements by their indices to maintain original relative order
        largest_k.sort(key=lambda x: x[1])

        # Extract the values for the result
        result = [num for (num, _) in largest_k]

        return result


# Unit Test: nums = [2,1,3,3], k = 2, Output: [3,3]
assert Solution.maxSubsequenceSum([2, 1, 3, 3], 2) == [3, 3]

# Unit Test: nums = [-1,-2,3,4], k = 3, Output: [-1,3,4]
assert Solution.maxSubsequenceSum([-1, -2, 3, 4], 3) == [-1, 3, 4]

# Unit Test: nums = [3,4,3,3], k = 2, Output: [3,4]
assert Solution.maxSubsequenceSum([3, 4, 3, 3], 2) == [3, 4]

print("All unit tests are passed")
