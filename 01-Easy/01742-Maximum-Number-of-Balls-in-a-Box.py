"""1742. Maximum Number of Balls in a Box
Link: https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
Difficulty: Easy
Description: You are working in a ball factory where you have n balls numbered from lowLimit up to
highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered
from 1 to infinity.
Your job at this factory is to put each ball in the box with a number equal to the sum of digits
of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6
and the ball number 10 will be put in the box number 1 + 0 = 1.
Given two integers lowLimit and highLimit, return the number of balls in the box with the most
balls."""


class Solution:
    @staticmethod
    def count_balls(lowLimit: int, highLimit: int) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the number of balls in each box
        balls_in_box = {}

        # Count the number of balls in each box from lowLimit to highLimit
        for ball in range(lowLimit, highLimit + 1):
            box = sum(int(digit) for digit in str(ball))
            balls_in_box[box] = balls_in_box.get(box, 0) + 1

        return max(balls_in_box.values())


# Unit Test: low_limit = 1, high_limit = 10, Output: 2
assert Solution.count_balls(1, 10) == 2

# Unit Test: low_limit = 5, high_limit = 15, Output: 2
assert Solution.count_balls(5, 15) == 2

# Unit Test: low_limit = 19, high_limit = 28, Output: 2
assert Solution.count_balls(19, 28) == 2

print("All unit tests are passed.")
