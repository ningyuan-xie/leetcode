"""3438. Find Valid Pair of Adjacent Digits in String
Link: https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/
Difficulty: Easy
Description: You are given a string s consisting only of digits. A valid pair is defined as two adjacent digits in s such that:
• The first digit is not equal to the second.
• Each digit in the pair appears in s exactly as many times as its numeric value.
Return the first valid pair found in the string s when traversing from left to right. If no valid pair exists, return an empty string."""


class Solution:
    @staticmethod
    def findValidPair(s: str) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        digit_count = {}
        for digit in s:
            digit_count[digit] = digit_count.get(digit, 0) + 1

        for i in range(len(s) - 1):
            first_digit = s[i]
            second_digit = s[i + 1]

            if first_digit != second_digit and digit_count[first_digit] == int(first_digit) and\
                  digit_count[second_digit] == int(second_digit):
                return first_digit + second_digit

        return ""


def unit_tests():
    # Input: s = "2523533", Output: "23"
    assert Solution.findValidPair("2523533") == "23"

    # Input: s = "221", Output: "21"
    assert Solution.findValidPair("221") == "21"

    # Input: s = "22", Output: ""
    assert Solution.findValidPair("22") == ""


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
