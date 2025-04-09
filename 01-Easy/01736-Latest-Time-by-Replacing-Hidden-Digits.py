"""1736. Latest Time by Replacing Hidden Digits
Link: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
Difficulty: Easy
Description: You are given a string time in the form of  hh:mm, where some of the digits in the
string are hidden (represented by ?).
The valid times are those inclusively between 00:00 and 23:59.
Return the latest valid time you can get from time by replacing the hidden digits."""


class Solution:
    @staticmethod
    def maximum_time(time: str) -> str:
        """Optimal Solution: Maximize digits. Time Complexity: O(1), Space Complexity: O(1)"""
        # Convert the time string to a list of characters
        time = list(time)

        # Handle the hour part
        if time[0] == '?':
            time[0] = '2' if time[1] in '0123?' else '1'
        if time[1] == '?':
            time[1] = '3' if time[0] == '2' else '9'

        # Handle the minute part
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'

        return ''.join(time)  # Convert list back to string


# Unit Test: time = "2?:?0", Output: "23:50"
assert Solution.maximum_time("2?:?0") == "23:50"

# Unit Test: time = "0?:3?", Output: "09:39"
assert Solution.maximum_time("0?:3?") == "09:39"

# Unit Test: time = "1?:22", Output: "19:22"
assert Solution.maximum_time("1?:22") == "19:22"

print("All unit tests are passed.")

