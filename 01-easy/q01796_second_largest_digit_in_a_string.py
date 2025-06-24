"""1796. Second Largest Digit in a String
Link: https://leetcode.com/problems/second-largest-digit-in-a-string/
Difficulty: Easy
Description: Given an alphanumeric string s, return the second largest numerical digit that appears
in s, or -1 if it does not exist.
An alphanumeric string is a string consisting of lowercase English letters and digits."""


class Solution:
    @staticmethod
    def second_largest_digit(s: str) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize a set to store unique digits
        digits = set()

        # Traverse the string and add digits to the set
        for char in s:
            if char.isdigit():
                digits.add(int(char))  # E.g. "dfa12321afd" -> {1, 2, 3}

        # Return the second largest digit if it exists
        if len(digits) < 2:
            return -1
        else:
            digits.remove(max(digits))
            return max(digits)


# Input: s = "dfa12321afd", Output: 2
assert Solution.second_largest_digit("dfa12321afd") == 2

# Input: s = "abc1111", Output: -1
assert Solution.second_largest_digit("abc1111") == -1

# Input: s = "abc", Output: -1
assert Solution.second_largest_digit("abc") == -1

print("All unit tests are passed.")
