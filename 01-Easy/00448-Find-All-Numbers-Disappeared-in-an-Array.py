"""448. Find All Numbers Disappeared in an Array
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Difficulty: Easy
Description: Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space."""

from typing import List


class Solution:
    @staticmethod
    def findDisappearedNumbers(nums: List[int]) -> List[int]:
        """Optimal Solution: Cyclic Sort. Time Complexity: O(n), Space Complexity: O(1).
        Cyclic sort maps each number nums[i] to its correct index nums[i] - 1: 1 at index 0, 2 at index 1, ..., n at index n-1."""
        n = len(nums)
        result = []

        # Cyclic sort
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                # Swap the elements to their correct positions
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Find the missing numbers
        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result


def unit_tests():
    # Input: nums = [4, 3, 2, 7, 8, 2, 3, 1], Output: [5, 6]
    assert Solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

    # Input: nums = [1, 1], Output: [2]
    assert Solution.findDisappearedNumbers([1, 1]) == [2]

    # Input: nums = [1], Output: []
    assert Solution.findDisappearedNumbers([1]) == []


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
