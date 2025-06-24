"""2437. Number of Valid Clock Times
Link: https://leetcode.com/problems/number-of-valid-clock-times/
Difficulty: Easy
Description: You are given a string of length 5 called time, representing the current time on a d
igital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible
time is "23:59".
In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a
digit from 0 to 9.
Return an integer answer, the number of valid clock times that can be created by replacing every ? with
a digit from 0 to 9."""

from typing import List


class Solution:
    @staticmethod
    def countTime(time: str) -> int:
        """Optimal Solution: Brute Force. Time Complexity: O(1), Space Complexity: O(1)."""
        # Count the number of valid times
        count = 0

        for h in range(24):
            for m in range(60):
                if (
                    (time[0] == "?" or time[0] == str(h // 10))  # time[0] ranges from 0 to 2
                    and (time[1] == "?" or time[1] == str(h % 10))  # time[1] ranges from 0 to 9
                    and (time[3] == "?" or time[3] == str(m // 10))  # time[3] ranges from 0 to 5
                    and (time[4] == "?" or time[4] == str(m % 10))  # time[4] ranges from 0 to 9
                ):
                    count += 1
        return count


# Input: time = "?5:00", Output: 2
assert Solution.countTime("?5:00") == 2

# Input: time = "0?:0?", Output: 100
assert Solution.countTime("0?:0?") == 100

# Input: time = "??:??", Output: 1440
assert Solution.countTime("??:??") == 1440

print("All unit tests are passed.")
