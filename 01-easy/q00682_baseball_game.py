"""682. Baseball Game
Link: https://leetcode.com/problems/baseball-game/
Difficulty: Easy
Description: You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
• An integer x.
  • Record a new score of x.
• '+'.
  • Record a new score that is the sum of the previous two scores.
• 'D'.
  • Record a new score that is the double of the previous score.
• 'C'.
  • Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid."""

from typing import List


class Solution:
    @staticmethod
    def calPoints(operations: List[str]) -> int:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        stack = []
        
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
                
        return sum(stack)


def unit_tests():
    # Input: ops = ["5", "2", "C", "D", "+"], Output: 30
    assert Solution.calPoints(["5", "2", "C", "D", "+"]) == 30

    # Input: ops = ["5", "-2", "4", "C", "D", "9", "+", "+"], Output: 27
    assert Solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
