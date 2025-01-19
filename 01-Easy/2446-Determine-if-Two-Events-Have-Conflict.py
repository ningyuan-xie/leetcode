"""2446. Determine if Two Events Have Conflict
Link: https://leetcode.com/problems/determine-if-two-events-have-conflict/
Difficulty: Easy
Description: You are given two arrays of strings that represent two inclusive events that happened on
the same day, event1 and event2, where:
- event1 = [startTime1, endTime1] and
- event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.
A conflict happens when two events have some non-empty intersection (i.e., some moment is common to
both events).
Return true if there is a conflict between two events. Otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def haveConflict(event1: List[str], event2: List[str]) -> bool:
        """Optimal Solution: String Manipulation. Time Complexity: O(1), Space Complexity: O(1)"""

        def convert_to_minutes(time: str) -> int:
            """Helper function to convert time to minutes"""
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes

        start1, end1 = map(convert_to_minutes, event1)  # ["01:15", "02:00"] -> 75, 120
        start2, end2 = map(convert_to_minutes, event2)

        # If Event1 starts before Event2 and ends after Event2 starts
        if start1 <= start2 <= end1:
            return True
        # If Event2 starts before Event1 and ends after Event1 starts
        elif start2 <= start1 <= end2:
            return True
        else:
            return False


# Unit Test: event1 = ["01:15", "02:00"], event2 = ["02:00", "03:00"], Output: True
assert Solution.haveConflict(["01:15", "02:00"], ["02:00", "03:00"]) is True

# Unit Test: event1 = ["01:00", "02:00"], event2 = ["01:20", "03:00"], Output: True
assert Solution.haveConflict(["01:00", "02:00"], ["01:20", "03:00"]) is True

# Unit Test: event1 = ["10:00", "11:00"], event2 = ["14:00", "15:00"], Output: False
assert Solution.haveConflict(["10:00", "11:00"], ["14:00", "15:00"]) is False

# Unit Test: event1 = ["06:35", "07:15"], event2 = ["16:41", "19:36"], Output: False
assert Solution.haveConflict(["06:35", "07:15"], ["16:41", "19:36"]) is False

# Unit Test: event1 = ["14:13", "22:08"], event2 = ["02:40","08:08"], Output: False
assert Solution.haveConflict(["14:13", "22:08"], ["02:40", "08:08"]) is False

print("All unit tests are passed")
