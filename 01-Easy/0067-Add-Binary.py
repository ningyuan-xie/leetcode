"""67. Add Binary
Link: https://leetcode.com/problems/add-binary/
Difficulty: Easy
Description: Given two binary strings a and b, return their sum as a binary string."""


class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        """Optimal Solution: Math. Time Complexity: O(max(n, m)), Space Complexity: O(max(n, m)
           Similar to 0066-Plus-One.py"""
        # Initialize result and carry
        result, carry = [], 0
        # Reverse the strings, so we can loop through the digits from RIGHT to LEFT
        a, b = a[::-1], b[::-1]
        # Loop through the maximum length to get every digit
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            # Calculate the total and get the remainder and carry
            total = digit_a + digit_b + carry
            remainder, carry = total % 2, total // 2
            # Add the remainder to the back of the result (reverted)
            result.append(str(remainder))
        # If there's a carry left, add it to the result
        if carry:
            result.append(str(carry))
        # Reverse the result (which is a list of str) and join them into a string
        return "".join(result[::-1])


# Unit Test: Input: a = "11", b = "1", Output: "100"
assert Solution.addBinary("11", "1") == "100"

# Unit Test: Input: a = "1010", b = "1011", Output: "10101"
assert Solution.addBinary("1010", "1011") == "10101"

# Unit Test: Input: a = "1", b = "0", Output: "1"
assert Solution.addBinary("1", "0") == "1"

print("All unit tests are passed")
