"""2409. Count Days Spent Together
Link: https://leetcode.com/problems/count-days-spent-together/
Difficulty: Easy
Description: Alice and Bob are traveling to Rome for separate business meetings.
You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city
from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates
arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD",
corresponding to the month and day of the date.
Return the total number of days that Alice and Bob are in Rome together.
You can assume that all dates occur in the same calendar year, which is not a leap year. Note that
the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]."""


class Solution:
    @staticmethod
    def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """Optimal Solution: String Manipulation. Time Complexity: O(1), Space Complexity: O(1)"""
        daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def getDays(date: str) -> int:
            """Helper function to get the total days from the beginning of the year"""
            month, day = int(date[:2]), int(date[3:])  # date = "08-15" -> month = 8, day = 15
            return sum(daysPerMonth[:month - 1]) + day

        arriveAlice, leaveAlice, arriveBob, leaveBob \
            = getDays(arriveAlice), getDays(leaveAlice), getDays(arriveBob), getDays(leaveBob)

        return max(0, min(leaveAlice, leaveBob) - max(arriveAlice, arriveBob) + 1)


# Unit Test: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19",
# Output: 3
assert (Solution.countDaysTogether("08-15", "08-18", "08-16", "08-19")
        == 3)

# Unit Test: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31",
# Output: 0
assert (Solution.countDaysTogether("10-01", "10-31", "11-01", "12-31")
        == 0)

print("All unit tests are passed.")
