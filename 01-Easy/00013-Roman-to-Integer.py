"""13. Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Description: Given a roman numeral, convert it to an integer."""


class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)"""
        # Create dictionary with key-value pairs
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Initialize sum
        sum_num = 0
        # Loop through input string
        for i in range(len(s)):
            # If the current value is less than the next value,
            # and we are not at the last index,
            # subtract the current value from the sum
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                sum_num -= roman_dict[s[i]]
            # Otherwise, add the current value to the sum
            else:
                sum_num += roman_dict[s[i]]
        return sum_num


# Input: s = "III", Output: 3
assert Solution.romanToInt("III") == 3

# Input: s = "IV", Output: 4
assert Solution.romanToInt("IV") == 4

# Input: s = "IX", Output: 9
assert Solution.romanToInt("IX") == 9

print("All unit tests are passed.")
