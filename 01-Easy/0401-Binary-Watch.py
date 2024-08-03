"""401. Binary Watch
Link: https://leetcode.com/problems/binary-watch/
Difficulty: Easy
Description: A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.
Given a non-negative integer n which represents the number of LEDs that are currently on,
return all possible times the watch could represent."""

from typing import List


class Solution:
    @staticmethod
    def readBinaryWatch(turnedOn: int) -> List[str]:
        """Optimal Solution: Brute Force. Time Complexity: O(1), Space Complexity: O(1)
           Constant time/space complexity because the number of possible times is fixed"""
        # Initialize a list to store the possible times
        times = []
        # Traverse the hours from 0 to 11
        for hour in range(12):
            # Traverse the minutes from 0 to 59
            for minute in range(60):
                # Count the number of LEDs that are currently on
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    # Hour 3 in binary is 0011 (2 LEDs on) and minute 15 in binary is 1111 (4 LEDs on)
                    # bin(3) = '0b11' and bin(15) = '0b1111'
                    # bin(3).count('1') = 2 and bin(15).count('1') = 4
                    times.append(f"{hour}:{minute:02d}")
        return times


# Unit Test: Input: turnedOn = 1,
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
assert Solution.readBinaryWatch(1) == ["0:01", "0:02", "0:04", "0:08", "0:16",
                                       "0:32", "1:00", "2:00", "4:00", "8:00"]

# Unit Test: Input: turnedOn = 9, Output: []
assert Solution.readBinaryWatch(9) == []

# Unit Test: Input: turnedOn = 0, Output: ["0:00"]
assert Solution.readBinaryWatch(0) == ["0:00"]

print("All unit tests are passed")
