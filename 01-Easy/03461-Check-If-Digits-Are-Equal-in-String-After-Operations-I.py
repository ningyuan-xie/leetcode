"""3461. Check If Digits Are Equal in String After Operations I
Link: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
Difficulty: Easy
Description: You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
• For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
• Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
Return true if the final two digits in s are the same; otherwise, return false."""


class Solution:
    @staticmethod
    def hasSameDigits(s: str) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Repeatedly reduce the string until it has exactly two digits
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_digit = (int(s[i]) + int(s[i + 1])) % 10
                new_s.append(str(new_digit))
            s = ''.join(new_s)
        return s[0] == s[1]


def unit_tests():
    # Input: s = "3902", Output: True
    assert Solution.hasSameDigits("3902") is True

    # Input: s = "34789", Output: False
    assert Solution.hasSameDigits("34789") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
