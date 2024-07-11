# Link: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Difficulty: Easy
# Description: Given an integer num, return a string representing its hexadecimal representation.
# For negative integers, two’s complement method is used. For example:
# -1 = 2^32 - 1 = 4294967295 = 0xffffffff; -2 = 2^32 - 2 = 4294967294 = 0xfffffffe

class Solution:
    # Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)
    # Similar to 0168-Excel-Sheet-Column-Title.py
    @staticmethod
    def toHex(num: int) -> str:
        # Edge case: if the number is 0, return "0"
        if num == 0:
            return "0"
        # Initialize a dictionary to map numbers to their hexadecimal representation
        hex_map = "0123456789abcdef"
        # Initialize a variable to store the hexadecimal representation
        hex_str = ""
        # Convert negative numbers to their two's complement representation
        if num < 0:
            num += 2 ** 32  # E.g., -1 = 2^32 - 1 = 4294967295 = 0xffffffff
        # Convert the number to its hexadecimal representation
        while num > 0:
            remainder = num % 16
            # Add the remainder to the front of the string
            hex_str = hex_map[remainder] + hex_str
            # Divide the number by 16 using floor division to get the next digit on the left
            num //= 16
        return hex_str


# Unit Test: Input: num = 26, Output: "1a"
assert Solution.toHex(26) == "1a"  # hex_str: hex_map[1] + hex_map[10] = "1a"

# Unit Test: Input: num = -1, Output: "ffffffff"
assert Solution.toHex(-1) == "ffffffff"

# Unit Test: Input: num = 0, Output: "0"
assert Solution.toHex(0) == "0"

print("All unit tests are passed")
