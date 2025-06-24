"""2549. Count Distinct Numbers on Board
Link: https://leetcode.com/problems/count-distinct-numbers-on-board/
Difficulty: Easy
Description: You are given a positive integer n, that is initially placed on a board. Every day,
for 10^9 days, you perform the following procedure:
- For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
- Then, place those numbers on the board.
Return the number of distinct integers present on the board after 10^9 days have elapsed.
Note:
- Once a number is placed on the board, it will remain on it until the end.
- % stands for the modulo operation. For example, 14 % 3 is 2."""

from typing import List


class Solution:
    @staticmethod
    def distinctIntegers(n: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1).
           Regardless how large n is, n % (n - 1) will always be 1. Therefore, recursively speaking,
           the distinct numbers on the board will always be n, n - 1, ..., 2, which is n - 1 numbers"""
        return n - 1 if n > 1 else 1

    @staticmethod
    def distinctIntegersRecursion(n: int) -> int:
        """Alternative Solution: Recursion. Time Complexity: O(n), Space Complexity: O(n)."""
        board = set()

        def updateBoard(x: int) -> None:
            """Helper function: Preorder DFS Traversal"""
            # Base Case: Stop recursion if x is already processed
            if x in board:
                return

            # Root Case: Add x to the board before exploring further
            board.add(x)

            # Recursive Case: Explore numbers i < x where x % i == 1
            for i in range(1, x):
                if x % i == 1 and i not in board:
                    updateBoard(i)

        # Start DFS recursion from n
        updateBoard(n)
        return len(board)


# Input: n = 5, Output: 4
assert Solution.distinctIntegersRecursion(5) == 4

# Input: n = 3, Output: 2
assert Solution.distinctIntegersRecursion(3) == 2

# Input: n = 1, Output: 1
assert Solution.distinctIntegers(1) == 1

print("All unit tests are passed.")
