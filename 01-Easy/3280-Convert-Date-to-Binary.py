"""3280. Convert Date to Binary
Link: https://leetcode.com/problems/convert-date-to-binary/
Difficulty: Easy
Description: You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.
date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.
Return the binary representation of date."""


class Solution:
    @staticmethod
    def convertDateToBinary(date: str) -> str:
        """Optimal Solution: String Manipulation & bin() function.
           Time Complexity: O(1), Space Complexity: O(1)"""
        # Split the date string into year, month, and day
        year, month, day = date.split('-')

        # Convert year, month, and day to binary strings without leading zeros
        year_bin = bin(int(year))[2:]  # [2:] to remove '0b' prefix
        month_bin = bin(int(month))[2:]
        day_bin = bin(int(day))[2:]

        # Concatenate the binary strings with '-' separator
        return f"{year_bin}-{month_bin}-{day_bin}"


# Unit Test: date = "2080-02-29", Output: "100000100000-10-11101"
assert Solution.convertDateToBinary("2080-02-29") == "100000100000-10-11101"

# Unit Test: date = "1900-01-01", Output: "11101101100-1-1"
assert Solution.convertDateToBinary("1900-01-01") == "11101101100-1-1"

print("All unit tests are passed")
