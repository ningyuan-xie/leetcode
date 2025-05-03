"""415. Add Strings
Link: https://leetcode.com/problems/add-strings/
Difficulty: Easy
Description: Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly."""


class Solution:
    @staticmethod
    def addStrings(num1: str, num2: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(max(m, n)), Space Complexity: O(1).
        Similar to 67. Add Binary."""
        m, n = len(num1), len(num2)
        result = []
        carry = 0

        # Traverse both strings from the end
        for i in range(max(m, n)):
            # Get the current digits and add them along with the carry
            digit_a = int(num1[m - 1 - i]) if i < m else 0
            digit_b = int(num2[n - 1 - i]) if i < n else 0
            total = digit_a + digit_b + carry

            # Calculate the new digit and carry
            result.append(str(total % 10))
            carry = total // 10

        # If there's a carry left, append it
        if carry:
            result.append(str(carry))

        # Reverse the result and join to form the final string
        return ''.join(result[::-1])


def unit_tests():
    # Input: num1 = "11", num2 = "123", Output: "134"
    assert Solution.addStrings("11", "123") == "134"

    # Input: num1 = "456", num2 = "77", Output: "533"
    assert Solution.addStrings("456", "77") == "533"

    # Input: num1 = "0", num2 = "0", Output: "0"
    assert Solution.addStrings("0", "0") == "0"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
