"""1360. Number of Days Between Two Dates
Link: https://leetcode.com/problems/number-of-days-between-two-dates/
Difficulty: Easy
Description: Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples."""


class Solution:
    @staticmethod
    def daysBetweenDates(date1: str, date2: str) -> int:
        """Optimal Solution: datetime module. Time Complexity: O(1), Space Complexity: O(1)
           Similar to 1185-Day-of-the-Week.py"""
        from datetime import datetime

        # Convert the string dates to datetime objects:
        # .strptime() parses the string to a datetime object
        date_format = "%Y-%m-%d"
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)

        # Return the absolute difference in days: .days returns the number of days between two dates
        return abs((d2 - d1).days)


# Input: date1 = "2019-06-29", date2 = "2019-06-30", Output: 1
assert Solution.daysBetweenDates("2019-06-29", "2019-06-30") == 1

# Input: date1 = "2020-01-15", date2 = "2019-12-31", Output: 15
assert Solution.daysBetweenDates("2020-01-15", "2019-12-31") == 15

# Input: date1 = "2020-01-15", date2 = "2019-12-31", Output: 15
assert Solution.daysBetweenDates("2020-01-15", "2019-12-31") == 15

print("All unit tests are passed.")
