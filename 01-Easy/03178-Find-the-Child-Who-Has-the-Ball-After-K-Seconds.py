"""3178. Find the Child Who Has the Ball After K Seconds
Link: https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds
Difficulty: Easy
Description: You are given two positive integers n and k. There are n children numbered from 0
to n - 1 standing in a queue in order from left to right.
Initially, child 0 holds a ball and the direction of passing the ball is towards the right
direction. After each second, the child holding the ball passes it to the child next to them.
Once the ball reaches either end of the line, i.e. child 0 or child n - 1, the direction of
passing is reversed.
Return the number of the child who receives the ball after k seconds."""


class Solution:
    @staticmethod
    def numberOfChild(n: int, k: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1).
           Same as 2582-Pass-the-Pillow"""
        # Calculate the number of complete rounds
        rounds = k // (n - 1)

        # Calculate the remaining time after complete rounds
        remaining_time = k % (n - 1)

        # Determine the final player based on the number of complete rounds and remaining time:
        # If rounds is even, the ball is passed in the same direction as the start
        if rounds % 2 == 0:
            return remaining_time
        # If rounds is odd, the ball is passed in the opposite direction
        else:
            return n - remaining_time - 1


# Unit Test: n = 3, k = 5, Output = 1
assert Solution.numberOfChild(3, 5) == 1

# Unit Test: n = 5, k = 6, Output = 2
assert Solution.numberOfChild(5, 6) == 2

# Unit Test: n = 4, k = 2, Output = 2
assert Solution.numberOfChild(4, 2) == 2

print("All unit tests are passed")
