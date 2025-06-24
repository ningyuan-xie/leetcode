"""1013. Partition Array Into Three Parts With Equal Sum
Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum
Difficulty: Easy
Description: Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])"""

from typing import List


class Solution:
    @staticmethod
    def canThreePartsEqualSum(arr: List[int]) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Calculate the total sum of the array
        total_sum = sum(arr)

        # If the total sum is not divisible by 3, return False
        if total_sum % 3 != 0:
            return False

        # Initialize the left and right pointers
        left, right = 0, len(arr) - 1

        # Initialize the left and right sums
        left_sum, right_sum = arr[left], arr[right]

        # Initialize the target sum
        target_sum = total_sum // 3

        # Move the left pointer to the right
        while left <= len(arr) - 3 and left_sum != target_sum:
            left += 1
            left_sum += arr[left]

        # Move the right pointer to the left
        while right >= 2 and right_sum != target_sum:
            right -= 1
            right_sum += arr[right]

        # Check if three parts are equal
        return left + 1 < right and left_sum == right_sum == target_sum


def unit_tests():
    # Input: arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], Output: True
    assert Solution.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) is True

    # Input: arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], Output: False
    assert Solution.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) is False

    # Input: arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4], Output: True
    assert Solution.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
