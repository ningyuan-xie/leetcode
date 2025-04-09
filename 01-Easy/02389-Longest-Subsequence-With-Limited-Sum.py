"""2389. Longest Subsequence With Limited Sum
Link: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
Difficulty: Easy
Description: You are given an integer array nums of length n, and an integer array queries of length m.
Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can
take from nums such that the sum of its elements is less than or equal to queries[i].
A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements."""

from typing import List
import bisect


class Solution:
    @staticmethod
    def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
        """Optimal Solution: Prefix Sum. Time Complexity: O(nlog(n)), Space Complexity: O(n)."""
        # Sort the nums array to consider the smallest elements first to maximize the subsequence length
        nums.sort()  # E.g. [4,5,2,1] -> [1,2,4,5]

        # Compute the prefix sum array
        prefix_sums = []
        current_sum = 0
        for num in nums:
            current_sum += num
            prefix_sums.append(current_sum)  # [1,2,4,5] -> [1,3,7,12]

        # For each query, use binary search to find the maximum subsequence length
        results = []
        for query in queries:
            # bisect_right returns the index where the query can be inserted in the prefix_sums array,
            # if equal then return the rightmost index
            idx = bisect.bisect_right(prefix_sums, query)
            results.append(idx)

        return results


# Unit Test: nums = [4,5,2,1], queries = [3,10,21], Output: [2,3,4]
assert Solution.answerQueries([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]

# Unit Test: nums = [2,3,4,5], queries = [1], Output: [0]
assert Solution.answerQueries([2, 3, 4, 5], [1]) == [0]

print("All unit tests are passed.")
