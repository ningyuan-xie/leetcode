"""1507. Reformat Date
Link: https://leetcode.com/problems/reformat-date/
Difficulty: Easy
Description: Given a date string in the form Day Month Year, where:
- Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
- Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
"Dec"}.
- Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:
- YYYY denotes the 4 digit year.
- MM denotes the 2 digit month.
- DD denotes the 2 digit day."""


class Solution:
    @staticmethod
    def reformatDate(date: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        # Define a mapping for month names to their respective numeric values
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        # Split the date string into parts (e.g. "20th Oct 2052" -> ["20th", "Oct", "2052"])
        day_str, month_str, year_str = date.split()

        # Extract numeric part from the day (e.g. "20th" -> "20")
        day = ''.join([c for c in day_str if c.isdigit()])

        # Convert the day to two digits if necessary (e.g. "20" -> "20", "1" -> "01")
        day = day.zfill(2)  # .zfill() method pads the string with zeros to the left

        # Get the numeric month from the month string (e.g. "Oct" -> "10")
        month = months[month_str]

        # Return the reformatted date (e.g. "20th Oct 2052" -> "2052-10-20")
        return f"{year_str}-{month}-{day}"


# Unit Test: date = "20th Oct 2052", Output: "2052-10-20"
assert Solution.reformatDate("20th Oct 2052") == "2052-10-20"

# Unit Test: date = "6th Jun 1933", Output: "1933-06-06"
assert Solution.reformatDate("6th Jun 1933") == "1933-06-06"

# Unit Test: date = "26th May 1960", Output: "1960-05-26"
assert Solution.reformatDate("26th May 1960") == "1960-05-26"

# Unit Test: date = "1st Jan 2000", Output: "2000-01-01"
assert Solution.reformatDate("1st Jan 2000") == "2000-01-01"

print("All unit tests are passed")
