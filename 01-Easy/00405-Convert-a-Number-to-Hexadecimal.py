"""405. Convert a Number to Hexadecimal
Link: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
Difficulty: Easy
Description: Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem."""


class Solution:
    @staticmethod
    def toHex(num: int) -> str:
        """Optimal Solution: Math. Time Complexity: O(log(n)), Space Complexity: O(1).
        Similar to 168. Excel Sheet Column Title."""
        # Handle the case for negative numbers using two's complement
        if num < 0:
            num += 2 ** 32

        # Define a mapping from integers to hexadecimal characters
        hex_map = "0123456789abcdef"
        hex_str = ""

        # Convert the number to hexadecimal
        while num > 0:
            hex_str = hex_map[num % 16] + hex_str
            num //= 16

        return hex_str if hex_str else "0"


def unit_tests():
    # Input: num = 26, Output: "1a"
    assert Solution.toHex(26) == "1a"  # hex_str: hex_map[1] + hex_map[10] = "1a"

    # Input: num = -1, Output: "ffffffff"
    assert Solution.toHex(-1) == "ffffffff"

    # Input: num = 0, Output: "0"
    assert Solution.toHex(0) == "0"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
