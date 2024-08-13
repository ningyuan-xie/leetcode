"""405. Convert a Number to Hexadecimal
Link: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
Difficulty: Easy
Description: Given an integer num, return a string representing its hexadecimal representation.
For negative integers, two’s complement method is used. For example:
-1 = 2^32 - 1 = 4294967295 = 0xffffffff; -2 = 2^32 - 2 = 4294967294 = 0xfffffffe"""


class Solution:
    @staticmethod
    def toHex(num: int) -> str:
        """Optimal Solution: Iterative Division.
           Time Complexity: O(log(n)), Space Complexity: O(log(n)).
           Similar to 0168-Excel-Sheet-Column-Title.py"""
        # Base case: If the number is 0, return "0"
        if num == 0:
            return "0"
        # Initialize the result and a dictionary to map numbers to their hexadecimal representation
        result = ""
        hex_map = "0123456789abcdef"
        # Convert negative numbers to their two's complement representation
        num += 2 ** 32 if num < 0 else 0  # E.g., -1 = 2^32 - 1 = 4294967295 = 0xffffffff
        # Convert the number to its hexadecimal representation from RIGHT to LEFT
        while num > 0:
            remainder = num % 16
            # Add the remainder to the front of the string
            result = hex_map[remainder] + result
            # Divide the number by 16 using floor division to move to the next digit on the left
            num //= 16
        return result


# Unit Test: Input: num = 26, Output: "1a"
assert Solution.toHex(26) == "1a"  # hex_str: hex_map[1] + hex_map[10] = "1a"

# Unit Test: Input: num = -1, Output: "ffffffff"
assert Solution.toHex(-1) == "ffffffff"

# Unit Test: Input: num = 0, Output: "0"
assert Solution.toHex(0) == "0"

print("All unit tests are passed")
