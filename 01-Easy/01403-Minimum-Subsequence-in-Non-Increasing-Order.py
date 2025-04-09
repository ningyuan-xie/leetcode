"""1403. Minimum Subsequence in Non-Increasing Order
Link: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order
Difficulty: Easy
Description: Given the array nums, obtain a subsequence of the array whose sum of elements is strictly
greater than the sum of the non included elements in such subsequence.
If there are multiple solutions, return the subsequence with minimum size and if there still exist
multiple solutions, return the subsequence with the maximum total sum of all its elements.
A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
Note that the solution with the given constraints is guaranteed to be unique. Also return the answer
sorted in non-increasing order."""

from typing import List


class Solution:
    @staticmethod
    def minSubsequence(nums: List[int]) -> List[int]:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n*log(n)), Space Complexity: O(n)"""
        # Sort the array in non-increasing order and sum all the elements
        nums.sort(reverse=True)  # E.g. [4, 3, 10, 9, 8] -> [10, 9, 8, 4, 3]
        total_sum = sum(nums)

        # Initialize the subsequence list and the sum of the subsequence
        subsequence_list, subsequence_sum = [], 0

        # Greedy approach: Add the elements from the largest to the smallest,
        # so that the size of the subsequence list is minimized
        for num in nums:
            subsequence_list.append(num)
            subsequence_sum += num
            # If the sum of the subsequence is greater than the sum of the non-included elements
            if subsequence_sum > total_sum - subsequence_sum:
                return subsequence_list


# Unit Test: nums = [4, 3, 10, 9, 8], Output: [10, 9]
assert Solution.minSubsequence([4, 3, 10, 9, 8]) == [10, 9]

# Unit Test: nums = [4, 4, 7, 6, 7], Output: [7, 7, 6]
assert Solution.minSubsequence([4, 4, 7, 6, 7]) == [7, 7, 6]

# Unit Test: nums = [6], Output: [6]
assert Solution.minSubsequence([6]) == [6]

print("All unit tests are passed")
