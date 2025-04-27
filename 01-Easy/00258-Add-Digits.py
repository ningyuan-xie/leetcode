"""258. Add Digits
Link: https://leetcode.com/problems/add-digits/
Difficulty: Easy
Description: Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Follow up: Could you do it without any loop/recursion in O(1) runtime?"""


class Solution:
    @staticmethod
    def addDigits(n: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1).
        The digital root of a number dr(n) = 1 + ((n - 1) % 9).
        E.g. dr(38) = 1 + ((38 - 1) % 9) = 1 + (37 % 9) = 1 + 1 = 2;
        E.g. dr(0) = 1 + ((0 - 1) % 9) = 1 + (-1 % 9) = 1 + -1 = 0."""
        # Digital Root Formula: 1 + (n - 1) % 9
        return 1 + ((n - 1) % 9) if n > 0 else 0


def unit_tests(): 
    # Input: num = 38, Output: 2
    assert Solution.addDigits(38) == 2

    # Input: num = 0, Output: 0
    assert Solution.addDigits(0) == 0

    # Input: num = 9, Output: 9
    assert Solution.addDigits(9) == 9


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
