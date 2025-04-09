"""682. Baseball Game
Link: https://leetcode.com/problems/baseball-game/
Difficulty: Easy
Description: You are keeping the scores for a baseball game with strange rules. At the beginning of
the game, you start with an empty record. You are given a list of strings operations, where
operations[i] is the ith operation you must apply to the record and is one of the following:
An integer x: Record a new score of x.
'+': Record a new score that is the sum of the previous two scores.
'D': Record a new score that is the double of the previous score.
'C': Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations."""

from typing import List


class Solution:
    @staticmethod
    def calPoints(operations: List[str]) -> int:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the stack
        stack = []

        # Iterate through the list of operations
        for op in operations:
            if op == '+':
                # Add the sum of the last two valid rounds to the stack
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Double the last valid round and add it to the stack
                stack.append(2 * stack[-1])
            elif op == 'C':
                # Remove the last valid round from the stack
                stack.pop()
            else:
                # Add the valid round to the stack
                stack.append(int(op))

        # Return the sum of the valid rounds
        return sum(stack)


# Unit Test: Input: ops = ["5", "2", "C", "D", "+"], Output: 30
assert Solution.calPoints(["5", "2", "C", "D", "+"]) == 30

# Unit Test: Input: ops = ["5", "-2", "4", "C", "D", "9", "+", "+"], Output: 27
assert Solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27

print("All unit tests are passed")
