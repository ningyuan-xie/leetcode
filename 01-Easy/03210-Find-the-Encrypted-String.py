"""3210. Find the Encrypted String
Link: https://leetcode.com/problems/find-the-encrypted-string
Difficulty: Easy
Description: You are given a string s and an integer k. Encrypt the string using the following
algorithm:
- For each character c in s, replace c with the kth character after c in the string (in a
cyclic manner).
Return the encrypted string."""


class Solution:
    @staticmethod
    def getEncryptedString(s: str, k: int) -> str:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(n)."""
        # Create a list to store the encrypted characters
        encrypted_chars = []

        # Iterate through each character in the string
        for i in range(len(s)):
            encrypted_chars.append(s[(i + k) % len(s)])

        return ''.join(encrypted_chars)


# Unit Test: s = "dart", k = 3, Output = "tdar"
assert Solution.getEncryptedString("dart", 3) == "tdar"

# Unit Test: s = "aaa", k = 1, Output = "aaa"
assert Solution.getEncryptedString("aaa", 1) == "aaa"

print("All unit tests are passed.")
