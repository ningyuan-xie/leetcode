"""1185. Day of the Week
Link: https://leetcode.com/problems/day-of-the-week/
Difficulty: Easy
Description: Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}."""


class Solution:
    @staticmethod
    def dayOfTheWeek(day: int, month: int, year: int) -> str:
        """Optimal Solution: datetime module. Time Complexity: O(1), Space Complexity: O(1)."""
        import datetime

        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # .datetime() creates a datetime object from the given date
        # .weekday() returns the day of the week as an integer (0 = Monday, 6 = Sunday)
        return days_of_week[datetime.datetime(year, month, day).weekday()]


def unit_tests():
    # Input: day = 31, month = 8, year = 2019, Output: "Saturday"
    assert Solution.dayOfTheWeek(31, 8, 2019) == "Saturday"

    # Input: day = 18, month = 7, year = 1999, Output: "Sunday"
    assert Solution.dayOfTheWeek(18, 7, 1999) == "Sunday"

    # Input: day = 15, month = 8, year = 1993, Output: "Sunday"
    assert Solution.dayOfTheWeek(15, 8, 1993) == "Sunday"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
