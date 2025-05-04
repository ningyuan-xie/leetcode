"""482. License Key Formatting
Link: https://leetcode.com/problems/license-key-formatting/
Difficulty: Easy
Description: You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
Return the reformatted license key."""


class Solution:
    @staticmethod
    def licenseKeyFormatting(s: str, k: int) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)."""
        # Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()

        # Calculate the length of the first group
        first_group_length = len(s) % k or k

        # Initialize the result with the first group
        result = [s[:first_group_length]]

        # Iterate through the string in steps of k
        for i in range(first_group_length, len(s), k):
            result.append(s[i:i + k])

        # Join the groups with dashes and return
        return "-".join(result)


def unit_tests():
    # Input: s = "5F3Z-2e-9-w", k = 4, Output: "5F3Z-2E9W"
    assert Solution.licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"

    # Input: s = "2-5g-3-J", k = 2, Output: "2-5G-3J"
    assert Solution.licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
