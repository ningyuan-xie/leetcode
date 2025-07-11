"""1304. Find N Unique Integers Sum up to Zero
Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
Difficulty: Easy
Description: Given an integer n, return any array containing n unique integers such that they add up to 0."""

from typing import List


class Solution:
    @staticmethod
    def sumZero(n: int) -> List[int]:
        """Optimal Solution: Alternating Numbers. Time Complexity: O(n), Space Complexity: O(n)."""
        arr = []

        # If n is odd, starts with 0
        if n % 2:
            arr.append(0)

        # Add alternating positive and negative numbers to the array
        for i in range(1, n // 2 + 1):
            arr.append(i)
            arr.append(-i)
        return arr


def unit_tests():
    # Input: n = 5, Output: [0, 1, -1, 2, -2]
    assert Solution.sumZero(5) == [0, 1, -1, 2, -2]

    # Input: n = 3, Output: [0, 1, -1]
    assert Solution.sumZero(3) == [0, 1, -1]

    # Input: n = 1, Output: [0]
    assert Solution.sumZero(1) == [0]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
