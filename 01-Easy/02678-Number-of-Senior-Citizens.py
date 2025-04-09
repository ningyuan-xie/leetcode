"""2678. Number of Senior Citizens
Link: https://leetcode.com/problems/number-of-senior-citizens/
Difficulty: Easy
Description: You are given a 0-indexed array of strings details. Each element of details provides
information about a given passenger compressed into a string of length 15. The system is such that:
- The first ten characters consist of the phone number of passengers.
- The next character denotes the gender of the person.
- The following two characters are used to indicate the age of the person.
- The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old."""

from typing import List


class Solution:
    @staticmethod
    def countSeniors(details: List[str]) -> int:
        """Optimal Solution: String Parsing. Time Complexity: O(n), Space Complexity: O(1)"""
        return sum(int(detail[11:13]) > 60 for detail in details)


# Unit Test: details = ["7868190130M7522","5303914400F9211","9273338290F4010"], Output: 2
assert Solution.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]) == 2

# Unit Test: details = ["1313579440F2036","2921522980M5644"], Output: 0
assert Solution.countSeniors(["1313579440F2036", "2921522980M5644"]) == 0

print("All unit tests are passed.")
