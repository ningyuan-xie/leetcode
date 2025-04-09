"""70. Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Description: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""


class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(1)"""
        # Base case for "one": if currently at last stair (top), 1 way to reach the top (stay there)
        # Base case for "two": if currently at second to last stair, 1 way to reach the top (1 step)
        one, two = 1, 1
        # Fibonacci sequence going from back to beginning: F(n) = F(n - 1) + F(n - 2)
        # as each PREVIOUS stair depends on the LATER two stairs: dynamic programming
        # To get to the F(n) Fibonacci number, loop n - 1 times because we already have F(0) and F(1)
        for i in range(n - 1):  # E.g. if n = 5, have stair 5 and 4, need stair 3, 2, 1, 0
            one, two = two, one + two
        return two


# Input: n = 2, Output: 2
assert Solution.climbStairs(2) == 2

# Input: n = 3, Output: 3
assert Solution.climbStairs(3) == 3

# Input: n = 4, Output: 5
assert Solution.climbStairs(4) == 5

print("All unit tests are passed.")
