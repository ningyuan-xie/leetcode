# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Description: You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        # Base case: if n is 1, return 1
        if n == 1:
            return 1
        # Initialize the first two steps
        first, second = 1, 2
        # Loop through the steps from 3 to n
        for i in range(3, n + 1):
            # Calculate the next step
            next_step = first + second
            # Update the first and second steps
            first, second = second, next_step
        # Return the last step
        return second


# Unit Test: Input: n = 2, Output: 2
assert Solution.climbStairs(2) == 2

# Unit Test: Input: n = 3, Output: 3
assert Solution.climbStairs(3) == 3

# Unit Test: Input: n = 4, Output: 5
assert Solution.climbStairs(4) == 5
print("All unit tests are passed")
