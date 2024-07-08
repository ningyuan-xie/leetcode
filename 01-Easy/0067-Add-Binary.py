# Link: https://leetcode.com/problems/add-binary/
# Difficulty: Easy
# Description: Given two binary strings a and b, return their sum as a binary string.

class Solution:
    # Optimal Solution: Math. Time Complexity: O(max(n, m)), Space Complexity: O(max(n, m))
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        # Initialize carry and result
        carry = 0
        result = []
        # Reverse the strings
        a, b = a[::-1], b[::-1]
        # Loop through the maximum length to get every digit
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            # Add the digits and the carry
            total = digit_a + digit_b + carry
            remainder = str(total % 2)  # E.g. 1 + 1 = 10 -> 0; 1 + 0 = 1 -> 1
            result.append(remainder)  # Add the remainder to the result
            carry = total // 2  # E.g. 1 + 1 = 10 -> 1; 1 + 0 = 1 -> 0

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
