"""415. Add Strings
Link: https://leetcode.com/problems/add-strings/
Difficulty: Easy
Description: Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string."""


class Solution:
    @staticmethod
    def addStrings(num1: str, num2: str) -> str:
        """Optimal Solution: Two Pointers. Time Complexity: O(max(n, m)), Space Complexity: O(max(n, m))
           Similar to 0067-Add-Binary.py"""
        # Initialize the sum and carry
        sum_str, carry = "", 0
        # Initialize pointers at the end of the strings
        i, j = len(num1) - 1, len(num2) - 1
        # Iterate through the strings from RIGHT to LEFT
        while i >= 0 or j >= 0:
            # Get the digits at the current positions
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            # Calculate the total and get the remainder and carry
            total = digit1 + digit2 + carry
            remainder, carry = total % 10, total // 10
            # Add the remainder to the front of the string
            sum_str = str(remainder) + sum_str
            # Move the pointers to the left
            i, j = i - 1, j - 1
        # If there is a carry left, add it to the front of the string
        return str(carry) + sum_str if carry else sum_str


# Unit Test: Input: num1 = "11", num2 = "123", Output: "134"
assert Solution.addStrings("11", "123") == "134"

# Unit Test: Input: num1 = "456", num2 = "77", Output: "533"
assert Solution.addStrings("456", "77") == "533"

# Unit Test: Input: num1 = "0", num2 = "0", Output: "0"
assert Solution.addStrings("0", "0") == "0"

print("All unit tests are passed")
