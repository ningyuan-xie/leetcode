"""1342. Number of Steps to Reduce a Number to Zero
Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Difficulty: Easy
Description: Given a non-negative integer num, return the number of steps to reduce it to zero."""


class Solution:
    @staticmethod
    def numberOfSteps(num: int) -> int:
        """Optimal Solution: Binary operation to reduce the number to zero.
           Time Complexity: O(log(n)), Space Complexity: O(1)."""
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1

            steps += 1

        return steps


# Input: num = 14, Output: 6
assert Solution.numberOfSteps(14) == 6

# Input: num = 8, Output: 4
assert Solution.numberOfSteps(8) == 4

# Input: num = 123, Output: 12
assert Solution.numberOfSteps(123) == 12

print("All unit tests are passed.")
