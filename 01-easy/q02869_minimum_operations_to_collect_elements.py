"""2869. Minimum Operations to Collect Elements
Link: https://leetcode.com/problems/minimum-operations-to-collect-elements/
Difficulty: Easy
Description: You are given an array nums of positive integers and an integer k.
In one operation, you can remove the last element of the array and add it to your collection.
Return the minimum number of operations needed to collect elements 1, 2, ..., k."""

from typing import List


class Solution:
    @staticmethod
    def minOperations(nums: List[int], k: int) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0
        target_list = list(range(1, k + 1))
        collection_list = []

        # Iterate the array in reverse order
        for i in range(len(nums) - 1, -1, -1):
            collection_list.append(nums[i])
            count += 1
            # Check if target list is in the collection list
            if set(target_list) <= set(collection_list):
                break
        # Return the minimum number of operations
        return count


# Unit Test: nums = [3,1,5,4,2], k = 2, Output: 4
assert Solution.minOperations([3, 1, 5, 4, 2], 2) == 4

# Unit Test: nums = [3,1,5,4,2], k = 5, Output: 5
assert Solution.minOperations([3, 1, 5, 4, 2], 5) == 5

# Unit Test: nums = [3,2,5,3,1], k = 3, Output: 4
assert Solution.minOperations([3, 2, 5, 3, 1], 3) == 4

print("All unit tests are passed.")
