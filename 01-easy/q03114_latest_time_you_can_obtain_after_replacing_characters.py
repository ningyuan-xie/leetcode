"""3114. Latest Time by Replacing Hidden Digits
Link: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits
Difficulty: Easy
Description: You are given a string s representing a 12-hour format time where some of the
digits (possibly none) are replaced with a "?".
12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59.
The earliest 12-hour time is 00:00, and the latest is 11:59.
You have to replace all the "?" characters in s with digits such that the time we obtain by the
resulting string is a valid 12-hour format time and is the latest possible.
Return the resulting string."""


class Solution:
    @staticmethod
    def findLatestTime(s: str) -> str:
        """Optimal Solution: Maximize digits. Time Complexity: O(1), Space Complexity: O(1).
           Similar to 1736. Latest Time by Replacing Hidden Digits"""
        # Convert the time string to a list of characters
        s = list(s)

        # Handle the hour part: max hour is 11
        if s[0] == '?':
            s[0] = '1' if s[1] in "?01" else '0'
        if s[1] == '?':
            s[1] = '9' if s[0] == '0' else '1'

        # Handle the minute part: max minute is 59
        if s[3] == '?':
            s[3] = '5'
        if s[4] == '?':
            s[4] = '9'

        return ''.join(s)  # Convert list back to string


# Input: s = "1?:?4", Output = "11:54"
assert Solution.findLatestTime("1?:?4") == "11:54"

# Input: s = "0?:5?", Output = "09:59"
assert Solution.findLatestTime("0?:5?") == "09:59"

# Input: s = "?3:12", Output = "03:12"
assert Solution.findLatestTime("?3:12") == "03:12"

# Input: s = "??:1?", Output = "11:19"
assert Solution.findLatestTime("??:1?") == "11:19"

print("All unit tests are passed.")
