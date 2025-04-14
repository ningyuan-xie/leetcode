"""3396. Minimum Number of Operations to Make Elements in Array Distinct
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
Difficulty: Easy
Description: You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
• Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct."""

from typing import List


class Solution:
    @staticmethod
    def minimumOperations(nums: List[int]) -> int:
        """Optimal Solution: Reverse Traversal. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(nums)
        count = [0] * (max(nums) + 1)
        duplicate_index = -1

        # Find the first duplicate from the end of the array
        for i in range(n - 1, -1, -1):
            count[nums[i]] += 1
            if count[nums[i]] == 2:
                duplicate_index = i
                break

        return (duplicate_index + 3) // 3 if duplicate_index != -1 else 0


def unit_tests():
    # Input: nums = [1,2,3,4,2,3,3,5,7], Output: 2
    assert Solution.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]) == 2

    # Input: nums = [4,5,6,4,4], Output: 2
    assert Solution.minimumOperations([4, 5, 6, 4, 4]) == 2

    # Input: nums = [6,7,8,9], Output: 0
    assert Solution.minimumOperations([6, 7, 8, 9]) == 0

    # Input: nums = [5,5], Output: 1
    assert Solution.minimumOperations([5, 5]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
