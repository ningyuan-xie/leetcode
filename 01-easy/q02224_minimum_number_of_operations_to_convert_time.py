"""2224. Minimum Number of Operations to Convert Time
Link: https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
Difficulty: Easy
Description: You are given two strings current and correct representing two 24-hour times.
24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59.
The earliest 24-hour time is 00:00, and the latest is 23:59.
In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this
operation any number of times.
Return the minimum number of operations needed to convert current to correct."""


class Solution:
    @staticmethod
    def convertTime(current: str, correct: str) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # Convert the time strings to minutes
        current_minutes = int(current[:2]) * 60 + int(current[3:])  # E.g. "02:30" -> 150
        correct_minutes = int(correct[:2]) * 60 + int(correct[3:])  # E.g. "04:35" -> 275

        # Calculate the difference in minutes
        diff = abs(current_minutes - correct_minutes)  # 275 - 150 = 125

        # Calculate the number of operations needed
        operations = 0
        for minutes in [60, 15, 5, 1]:
            operations += diff // minutes
            diff %= minutes

        return operations


# Unit Test: current = "02:30", correct = "04:35", Output: 3
assert Solution.convertTime("02:30", "04:35") == 3

# Unit Test: current = "11:00", correct = "11:01", Output: 1
assert Solution.convertTime("11:00", "11:01") == 1

print("All unit tests are passed.")
