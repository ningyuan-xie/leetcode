"""3498. Reverse Degree of a String
Link: https://leetcode.com/problems/reverse-degree-of-a-string/
Difficulty: Easy
Description: Given a string s, calculate its reverse degree.
The reverse degree is calculated as follows:
1. For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
2. Sum these products for all characters in the string.
Return the reverse degree of s."""


class Solution:
    @staticmethod
    def reverseDegree(s: str) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        result = 0
        n = len(s)

        # Calculate the reverse degree
        for i in range(n):
            # Calculate the position of the character in the reversed alphabet
            char_value = 26 - (ord(s[i]) - ord('a'))
            # Multiply by its position in the string (1-indexed)
            result += char_value * (i + 1)
        return result


def unit_tests():
    # Input: s = "abc", Output: 148
    assert Solution.reverseDegree("abc") == 148

    # Input: s = "zaza", Output: 160
    assert Solution.reverseDegree("zaza") == 160


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
