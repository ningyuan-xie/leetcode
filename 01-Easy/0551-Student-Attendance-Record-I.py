"""551. Student Attendance Record I
Link: https://leetcode.com/problems/student-attendance-record-i/
Difficulty: Easy
Description: You are given a string representing an attendance record for a student
where each character signifies whether the student was absent, late, or present on that day.
The record only contains the following three characters:
'A': Absent.'L': Late. 'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:
The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise."""


class Solution:
    @staticmethod
    def checkRecord(s: str) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the absent and late counters
        absent_count, late_count = 0, 0
        # Iterate through the attendance record
        for record in s:
            # 1. Check if the student was absent
            if record == 'A':
                absent_count += 1
                late_count = 0  # if absent, cannot be late, so reset the late counter
                if absent_count >= 2:  # check if the student was absent for 2 days
                    return False
            # 2. Check if the student was late
            elif record == 'L':
                late_count += 1
                if late_count >= 3:  # check if the student was late for 3 days
                    return False
            else:
                late_count = 0  # if present, cannot be late, so reset the late counter
        return True


# Unit Test: Input: s = "PPALLP", Output: True
assert Solution.checkRecord("PPALLP") == True

# Unit Test: Input: s = "PPALLL", Output: False
assert Solution.checkRecord("PPALLL") == False

# Unit Test: Input: s = "PPALLL", Output: False
assert Solution.checkRecord("PPALLL") == False

print("All unit tests are passed")
