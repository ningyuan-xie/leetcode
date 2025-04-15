"""70. Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Description: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""


class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(1).
        1st step: 1 way; 2nd step: 2 ways;
        3rd step: 1st step = 1 then 2 left (2 ways); 1st step = 2 then 1 left (1 way); 2 + 1 = 3 ways;
        4th step: 1st step = 1 then 3 left (3 ways); 1st step = 2 then 2 left (2 way); 3 + 2 = 5 ways;
        nth step: 1st step = 1 then (n-1) left; 1st step = 2 then (n-2) left; (n-1) + (n-2) ways."""
        if n <= 2:
            return n

        first, second = 1, 2
        # Climb(x) = Climb(x-1) + Climb(x-2)
        for _ in range(3, n + 1):
            first, second = second, first + second
        return second


def unit_tests():
    # Input: n = 2, Output: 2
    assert Solution.climbStairs(2) == 2

    # Input: n = 3, Output: 3
    assert Solution.climbStairs(3) == 3

    # Input: n = 4, Output: 5
    assert Solution.climbStairs(4) == 5


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
