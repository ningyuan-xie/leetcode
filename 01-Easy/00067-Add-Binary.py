"""67. Add Binary
Link: https://leetcode.com/problems/add-binary/
Difficulty: Easy
Description: Given two binary strings a and b, return their sum as a binary string."""


class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        """Optimal Solution: Binary Addition. Time Complexity: O(max(m, n)), Space Complexity: O(1)"""
        m, n = len(a), len(b)
        result = []
        carry = 0

        # Traverse both strings from the end
        for i in range(max(m, n)):
            # Get the current digits and add them along with the carry
            digit_a = int(a[m - 1 - i]) if i < m else 0
            digit_b = int(b[n - 1 - i]) if i < n else 0
            total = digit_a + digit_b + carry

            # Calculate the new digit and carry
            result.append(str(total % 2))
            carry = total // 2

        # If there's a carry left, append it
        if carry:
            result.append(str(carry))

        # Reverse the result and join to form the final binary string
        return ''.join(result[::-1])


def unit_tests():
    # Input: a = "11", b = "1", Output: "100"
    assert Solution.addBinary("11", "1") == "100"

    # Input: a = "1010", b = "1011", Output: "10101"
    assert Solution.addBinary("1010", "1011") == "10101"

    # Input: a = "1", b = "0", Output: "1"
    assert Solution.addBinary("1", "0") == "1"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
