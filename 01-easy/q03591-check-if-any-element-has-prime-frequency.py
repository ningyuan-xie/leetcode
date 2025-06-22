"""3591. Check if Any Element Has Prime Frequency
Link: https://leetcode.com/problems/check-if-any-element-has-prime-frequency/
Difficulty: Easy
Description: You are given an integer array nums.
Return true if the frequency of any element of the array is prime, otherwise, return false.
The frequency of an element x is the number of times it occurs in the array.
A prime number is a natural number greater than 1 with only two factors, 1 and itself."""

from typing import List


class Solution:
    @staticmethod
    def checkPrimeFrequency(nums: List[int]) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        def is_prime(number: int) -> bool:
            """Helper function to check if a number is prime."""
            if number < 2:
                return False
            for num in range(2, int(number ** 0.5) + 1):
                if number % num == 0:
                    return False
            return True

        for value in freq.values():
            if is_prime(value) is True:
                return True
        
        return False


def unit_tests():
    # Input: nums = [1,2,3,4,5,4], Output: true
    assert Solution.checkPrimeFrequency([1, 2, 3, 4, 5, 4]) is True

    # Input: nums = [1,2,3,4,5], Output: false
    assert Solution.checkPrimeFrequency([1, 2, 3, 4, 5]) is False

    # Input: nums = [2,2,2,4,4], Output: true
    assert Solution.checkPrimeFrequency([2, 2, 2, 4, 4]) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
