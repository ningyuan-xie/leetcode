# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy (Dynamic Programming)
# Description: You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        # Base case for "two": if currently at final stair, 1 way to reach the top
        # Base case for "one": if currently at second to last stair, 1 way to reach the top
        one, two = 1, 1
        # Fibonacci sequence going from back to beginning: f(n) = f(n-1) + f(n-2)
        # as each PREVIOUS stair depends on the LATER two stairs: dynamic programming
        for i in range(n-1):  # E.g. if n = 5, have stair 5 and 4, need stair 3, 2, 1, 0
            one, two = one + two, one
        return one


# Unit Test: Input: n = 2, Output: 2
assert Solution.climbStairs(2) == 2

# Unit Test: Input: n = 3, Output: 3
assert Solution.climbStairs(3) == 3

# Unit Test: Input: n = 4, Output: 5
assert Solution.climbStairs(4) == 5

print("All unit tests are passed")
