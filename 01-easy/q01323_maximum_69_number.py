"""1323. Maximum 69 Number
Link: https://leetcode.com/problems/maximum-69-number/
Difficulty: Easy
Description: Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6)."""


class Solution:
    @staticmethod
    def maximum69Number(num: int) -> int:
        """Optimal Solution: Convert the number to a string and replace the first '6' with '9'.
           Time Complexity: O(n), Space Complexity: O(n)."""
        # Only replace the first '6' with '9' to get the maximum number
        return int(str(num).replace('6', '9', 1))


# Input: num = 9669, Output: 9969
assert Solution.maximum69Number(9669) == 9969

# Input: num = 9996, Output: 9999
assert Solution.maximum69Number(9996) == 9999

# Input: num = 9999, Output: 9999
assert Solution.maximum69Number(9999) == 9999

print("All unit tests are passed.")
