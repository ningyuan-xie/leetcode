"""2670. Find the Distinct Difference Array
Link: https://leetcode.com/problems/find-the-distinct-difference-array/
Difficulty: Easy
Description: You are given a 0-indexed array nums of length n.
The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the
number of distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of
distinct elements in the prefix nums[0, ..., i].
Return the distinct difference array of nums.
Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j
inclusive. Particularly, if i > j then nums[i, ..., j] denotes an empty subarray."""

from typing import List


class Solution:
    @staticmethod
    def distinctDifferenceArray(nums: List[int]) -> List[int]:
        """Optimal Solution: Hash Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize variables to track the number of distinct elements in the prefix and suffix
        distinct_diff = []

        # Iterate through the array
        for i in range(len(nums)):
            prefix = set(nums[:i + 1])
            suffix = set(nums[i + 1:])
            distinct_diff.append(len(prefix) - len(suffix))

        # Return the distinct difference array
        return distinct_diff


# Unit Test: nums = [1,2,3,4,5], Output: [-3,-1,1,3,5]
assert Solution.distinctDifferenceArray([1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5]

# Unit Test: nums = [3,2,3,4,2], Output: [-2,-1,0,2,3]
assert Solution.distinctDifferenceArray([3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3]

print("All unit tests are passed.")
