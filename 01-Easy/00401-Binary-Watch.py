"""401. Binary Watch
Link: https://leetcode.com/problems/binary-watch/
Difficulty: Easy
Description: A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.
The hour must not contain a leading zero.
• For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.
• For example, "10:2" is not valid. It should be "10:02"."""

from typing import List


class Solution:
    @staticmethod
    def readBinaryWatch(turnedOn: int) -> List[str]:
        """Optimal Solution: Brute Force. Time Complexity: O(1), Space Complexity: O(1)."""
        times = []

        for hour in range(12):
            for minute in range(60):
                # Count the number of LEDs that are currently on
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    times.append(f"{hour}:{minute:02d}")
        return times


def unit_tests():
    # Input: turnedOn = 1, Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    assert Solution.readBinaryWatch(1) == ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]

    # Input: turnedOn = 9, Output: []
    assert Solution.readBinaryWatch(9) == []

    # Input: turnedOn = 0, Output: ["0:00"]
    assert Solution.readBinaryWatch(0) == ["0:00"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
