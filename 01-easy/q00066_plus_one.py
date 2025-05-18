"""66. Plus One
Link: https://leetcode.com/problems/plus-one/
Difficulty: Easy
Description: You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits."""

from typing import List


class Solution:
    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        """Optimal Solution: Reverse Traversal. Time Complexity: O(n), Space Complexity: O(1)."""
        n = len(digits)

        for i in range(n - 1, -1, -1):
            # If the digit is less than 9, we can simply increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            else:
                digits[i] = 0

        # If all digits are 9, we need to add an additional digit at the beginning
        return [1] + digits


def unit_tests():
    # Input: digits = [1, 2, 3], Output: [1, 2, 4]
    assert Solution.plusOne([1, 2, 3]) == [1, 2, 4]

    # Input: digits = [4, 3, 2, 1], Output: [4, 3, 2, 2]
    assert Solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

    # Input: digits = [0], Output: [1]
    assert Solution.plusOne([0]) == [1]

    # Input: digits = [9], Output: [1, 0]
    assert Solution.plusOne([9]) == [1, 0]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
