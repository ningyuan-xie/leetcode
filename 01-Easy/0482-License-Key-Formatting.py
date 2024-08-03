"""482. License Key Formatting
Link: https://leetcode.com/problems/license-key-formatting/
Difficulty: Easy
Description: You are given a license key represented as a string S which consists only
alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.
You are also given an integer k.
We want to reformat the string s such that each group contains exactly k characters,
except for the first group, which could be shorter than k but still must contain at least one character.
Furthermore, there must be a dash inserted between two groups,
and you should convert all lowercase letters to uppercase. Return the reformatted license key."""


class Solution:
    @staticmethod
    def licenseKeyFormatting(s: str, k: int) -> str:
        """Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)"""
        # Remove the dashes and convert all lowercase letters to uppercase
        s = s.replace("-", "").upper()  # E.g. s = "5F3Z-2e-9-w" -> "5F3Z2E9W"
        # Calculate the length of the first group
        first_group = len(s) % k  # s = "5F3Z2E9W", k = 4 -> first_group = 0
        # Initialize the reformatted license key
        license_key = s[:first_group]  # first_group = 0 -> license_key = ""
        # Iterate through the remaining groups
        for i in range(first_group, len(s), k):  # 3rd parameter k: increment by k each loop
            # Add a dash and the group to the reformatted license key
            if license_key:
                license_key += "-"  # Append a dash only if the current license key is not empty
            license_key += s[i:i + k]
        return license_key


# Unit Test: Input: s = "5F3Z-2e-9-w", k = 4, Output: "5F3Z-2E9W"
# First Group: "", Remaining Groups: "5F3Z", "2E9W"
assert Solution.licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"

# Unit Test: Input: s = "2-5g-3-J", k = 2, Output: "2-5G-3J"
# First Group: "2", Remaining Groups: "5G", "3J"
assert Solution.licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"

print("All unit tests are passed")
