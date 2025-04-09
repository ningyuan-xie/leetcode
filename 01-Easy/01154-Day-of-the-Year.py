"""1154. Day of the Year
Link: https://leetcode.com/problems/day-of-the-year/
Difficulty: Easy
Description: Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
return the day number of the year."""


class Solution:
    @staticmethod
    def dayOfYear(date: str) -> int:
        """Optimal Solution: Calculate day. Time Complexity: O(1), Space Complexity: O(1)"""
        # Initialize the number of days in each month
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Parse the year, month, and day from the input date
        year, month, day = map(int, date.split("-"))  # map applies int() to each element

        # Check if the year is a leap year
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

        # Calculate the day of the year = previous months + current month + leap year 1 day
        day_of_year = sum(days_in_month[:month]) + day + (month > 2 and is_leap_year)

        return day_of_year


# Unit Test: date = "2019-01-09", Output: 9
assert Solution.dayOfYear("2019-01-09") == 9

# Unit Test: date = "2019-02-10", Output: 41
assert Solution.dayOfYear("2019-02-10") == 41

# Unit Test: date = "2003-03-01", Output: 60
assert Solution.dayOfYear("2003-03-01") == 60

print("All unit tests are passed")
