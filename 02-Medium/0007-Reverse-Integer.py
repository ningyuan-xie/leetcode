"""7. Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/
Difficulty: Medium
Description: Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
then return 0."""


class Solution:
    # Optimal Solution: Math. Time Complexity: O(log(x)), Space Complexity: O(1)
    # Similar to the reverseBits method in 01-Easy/0190-Reverse-Bits.py
    @staticmethod
    def reverse(x: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(log(x)), Space Complexity: O(1)
           Similar to the reverseBits method in 01-Easy/0190-Reverse-Bits.py"""
        # Initialize the reversed integer
        reversed_x = 0
        # Initialize the sign of the integer
        sign = 1 if x > 0 else -1
        # Convert the given integer to a positive integer
        x = abs(x)
        # Continue the process until the given integer is 0
        while x > 0:
            # Extract the rightmost digit
            digit = x % 10  # 123 -> 3; 12 -> 2; 1 -> 1
            # Shift the result to the left by 1 bit, leaving room for the next bit to be added
            reversed_x = reversed_x * 10 + digit  # 3 -> 32 -> 321
            # Remove the rightmost digit that was just added to the result
            x //= 10  # 123 -> 12 -> 1 -> 0
        # Return the reversed integer with the sign
        return sign * reversed_x if reversed_x <= 2 ** 31 - 1 else 0


# Unit Test: Input: x = 123, Output: 321
assert Solution.reverse(123) == 321

# Unit Test: Input: x = -123, Output: -321
assert Solution.reverse(-123) == -321

# Unit Test: Input: x = 120, Output: 21
assert Solution.reverse(120) == 21

# Unit Test: Input: x = 0, Output: 0
assert Solution.reverse(0) == 0

print("All unit tests are passed")
