"""2011. Final Value of Variable After Performing Operations
Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
Difficulty: Easy
Description: There is a programming language with only four operations and one variable X:
- ++X and X++ increments the value of the variable X by 1.
- --X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.
Given an array of strings operations containing a list of operations, return the final value of X
after performing all the operations."""

from typing import List


class Solution:
    @staticmethod
    def finalValueAfterOperations(operations: List[str]) -> int:
        """Optimal Solution: One-Liner. Time Complexity: O(n), Space Complexity: O(1)."""
        return sum(1 if "++" in operation else -1 for operation in operations)


# Unit Test: operations = ["--X", "X++", "X++"], Output: 1
assert Solution.finalValueAfterOperations(["--X", "X++", "X++++"]) == 1

# Unit Test: operations = ["++X", "++X", "X++"], Output: 3
assert Solution.finalValueAfterOperations(["++X", "++X", "X++"]) == 3

# Unit Test: operations = ["X++", "++X", "--X", "X--"], Output: 0
assert Solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0

print("All unit tests are passed.")
