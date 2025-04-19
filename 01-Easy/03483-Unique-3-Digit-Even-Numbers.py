"""3483. Unique 3-Digit Even Numbers
Link: https://leetcode.com/problems/unique-3-digit-even-numbers/
Difficulty: Easy
Description: You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.
Note: Each copy of a digit can only be used once per number, and there may not be leading zeros."""

from typing import List


class Solution:
    @staticmethod
    def countEvenNumbers(digits: List[int]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n^3), Space Complexity: O(n)."""
        n = len(digits)
        even_count = set()

        # Check every combination of 3 digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Generate a 3-digit number
                    if i != j and j != k and i != k and digits[i] != 0 and digits[k] % 2 == 0:
                        digit_number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        even_count.add(digit_number)
        return len(even_count)


def unit_tests():
    # Input: digits = [1,2,3,4], Output: 12
    assert Solution.countEvenNumbers([1, 2, 3, 4]) == 12

    # Input: digits = [0,2,2], Output: 2
    assert Solution.countEvenNumbers([0, 2, 2]) == 2

    # Input: digits = [6,6,6], Output: 1
    assert Solution.countEvenNumbers([6, 6, 6]) == 1

    # Input: digits = [1,3,5], Output: 0
    assert Solution.countEvenNumbers([1, 3, 5]) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
