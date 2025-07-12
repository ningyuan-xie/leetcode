"""1317. Convert Integer to the Sum of Two No-Zero Integers
Link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
Difficulty: Easy
Description: No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
Given an integer n, return a list of two integers [a, b] where:
• a and b are No-Zero integers.
• a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them."""

from typing import List


class Solution:
    @staticmethod
    def getNoZeroIntegers(n: int) -> List[int]:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1)."""
        # Traverse all possible values of A from 1 to n - 1
        for A in range(1, n):
            # If A and n - A don't contain 0, then return [A, n - A]
            if '0' not in str(A) and '0' not in str(n - A):
                return [A, n - A]

        return []


def unit_tests():
    # Input: n = 2, Output: [1, 1]
    assert Solution.getNoZeroIntegers(2) == [1, 1]

    # Input: n = 11, Output: [2, 9]
    assert Solution.getNoZeroIntegers(11) == [2, 9]

    # Input: n = 10000, Output: [1, 9999]
    assert Solution.getNoZeroIntegers(10000) == [1, 9999]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
