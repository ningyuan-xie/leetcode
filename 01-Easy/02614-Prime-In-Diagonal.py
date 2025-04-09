"""2614. Prime In Diagonal
Link: https://leetcode.com/problems/prime-in-diagonal/
Difficulty: Easy
Description: You are given a 0-indexed two-dimensional integer array nums.
Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime
is present on any of the diagonals, return 0.
Note that:
- An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and
itself.
- An integer val is on one of the diagonals of nums if there exists an integer i for which
nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val."""

from typing import List


class Solution:
    @staticmethod
    def diagonalPrime(nums: List[List[int]]) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize variables to track the maximum prime number and its sum
        max_prime = 0
        n = len(nums)

        def is_prime(number: int) -> bool:
            """Helper function to check if a number is prime"""
            if number < 2:
                return False
            for num in range(2, int(number ** 0.5) + 1):
                if number % num == 0:
                    return False
            return True

        # Iterate through the diagonal elements of the matrix
        for i in range(n):
            if is_prime(nums[i][i]):  # Check primary diagonal
                max_prime = max(max_prime, nums[i][i])
            if is_prime(nums[i][n - i - 1]):  # Check secondary diagonal
                max_prime = max(max_prime, nums[i][n - i - 1])

        return max_prime


# Unit Test: nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]], Output: 11
assert Solution.diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]) == 11

# Unit Test: nums = [[1, 2, 3], [5, 17, 7], [9, 11, 10]], Output: 17
assert Solution.diagonalPrime([[1, 2, 3], [5, 17, 7], [9, 11, 10]]) == 17

print("All unit tests are passed.")
