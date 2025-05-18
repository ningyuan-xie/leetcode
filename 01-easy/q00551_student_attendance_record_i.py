"""551. Student Attendance Record I
Link: https://leetcode.com/problems/student-attendance-record-i/
Difficulty: Easy
Description: You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
• 'A': Absent.
• 'L': Late.
• 'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:
• The student was absent ('A') for strictly fewer than 2 days total.
• The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise."""


class Solution:
    @staticmethod
    def checkRecord(s: str) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        absent_count = 0
        late_streak = 0
        
        for char in s:
            if char == 'A':
                absent_count += 1
                late_streak = 0
                if absent_count >= 2:
                    return False
            elif char == 'L':
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:  # 'P'
                late_streak = 0
                
        return True


def unit_tests():
    # Input: s = "PPALLP", Output: True
    assert Solution.checkRecord("PPALLP") is True

    # Input: s = "PPALLL", Output: False
    assert Solution.checkRecord("PPALLL") is False

    # Input: s = "PPALLL", Output: False
    assert Solution.checkRecord("PPALLL") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
