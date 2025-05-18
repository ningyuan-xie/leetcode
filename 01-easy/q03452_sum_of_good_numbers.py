"""3452. Sum of Good Numbers
Link: https://leetcode.com/problems/sum-of-good-numbers/
Difficulty: Easy
Description: Given an array of integers nums and an integer k, an element nums[i] is considered good if it is strictly greater than the elements at indices i - k and i + k (if those indices exist). If neither of these indices exists, nums[i] is still considered good.
Return the sum of all the good elements in the array."""

from typing import List


class Solution:
    @staticmethod
    def sumOfGoodNumbers(nums: List[int], k: int) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        good_sum = 0
        n = len(nums)

        for i in range(n):
            if (i - k < 0 or nums[i] > nums[i - k]) and (i + k >= n or nums[i] > nums[i + k]):
                good_sum += nums[i]

        return good_sum
    

def unit_tests():
    # Input: nums = [1,3,2,1,5,4], k = 2, Output: 12
    assert Solution.sumOfGoodNumbers([1, 3, 2, 1, 5, 4], 2) == 12

    # Input: nums = [2,1], k = 1, Output: 2
    assert Solution.sumOfGoodNumbers([2, 1], 1) == 2


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
