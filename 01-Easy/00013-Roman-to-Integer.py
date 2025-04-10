"""13. Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Description: Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer."""


class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
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
        for i in range(len(s)):
            # If the current value is less than the next value, and we are not at the last index, subtract the current value from the sum
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                sum_num -= roman_dict[s[i]]
            # Otherwise, add the current value to the sum
            else:
                sum_num += roman_dict[s[i]]
        return sum_num


def unit_tests():
    # Input: s = "III", Output: 3
    assert Solution.romanToInt("III") == 3

    # Input: s = "IV", Output: 4
    assert Solution.romanToInt("IV") == 4

    # Input: s = "IX", Output: 9
    assert Solution.romanToInt("IX") == 9


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
