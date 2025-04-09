"""2769. Find the Maximum Achievable Number
Link: https://leetcode.com/problems/find-the-maximum-achievable-number/
Difficulty: Easy
Description: Given two integers, num and t. A number x is achievable if it can become equal to num
after applying the following operation at most t times:
- Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
Return the maximum possible value of x."""


class Solution:
    @staticmethod
    def theMaximumAchievableX(num: int, t: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)"""
        return num + t * 2


# Unit Test: num = 4, t = 1, Output: 6
assert Solution.theMaximumAchievableX(4, 1) == 6

# Unit Test: num = 3, t = 2, Output: 7
assert Solution.theMaximumAchievableX(3, 2) == 7

print("All unit tests are passed")
