"""1185. Day of the Week
Link: https://leetcode.com/problems/day-of-the-week/
Difficulty: Easy
Description: Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday"}."""


class Solution:
    @staticmethod
    def dayOfTheWeek(day: int, month: int, year: int) -> str:
        """Optimal Solution: Zeller's Congruence (used to calculate the day of the week for any date).
           Time Complexity: O(1), Space Complexity: O(1)"""
        # Initialize the days of the week, starting from Saturday
        days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        # In Zeller's Congruence, Jan & Feb are considered as 13th & 14th months of the previous year
        if month < 3:
            month += 12
            year -= 1

        # Calculate century (c) and year within the century (y)
        c, y = year // 100, year % 100  # E.g. 2019 -> c = 20, y = 19

        # Zeller's Congruence formula
        w = ((day
             + 13 * (month + 1) // 5  # A term that adjusts the month to fit the formula requirements
             + y
             + y // 4  # Leap year adjustment
             + c // 4  # Century adjustment
             - 2 * c)  # A correction factor for the century.
             % 7)

        # Return the day of the week
        return days_of_week[w]

    @staticmethod
    def dayOfTheWeekDateTime(day: int, month: int, year: int) -> str:
        """Alternative Solution: datetime module. Time Complexity: O(1), Space Complexity: O(1)"""
        import datetime

        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # .datetime() creates a datetime object from the given date
        # .weekday() returns the day of the week as an integer (0 = Monday, 6 = Sunday)
        return days_of_week[datetime.datetime(year, month, day).weekday()]


# Unit Test: day = 31, month = 8, year = 2019, Output: "Saturday"
assert Solution.dayOfTheWeek(31, 8, 2019) == "Saturday"

# Unit Test: day = 18, month = 7, year = 1999, Output: "Sunday"
assert Solution.dayOfTheWeek(18, 7, 1999) == "Sunday"

# Unit Test: day = 15, month = 8, year = 1993, Output: "Sunday"
assert Solution.dayOfTheWeekDateTime(15, 8, 1993) == "Sunday"

print("All unit tests are passed.")
