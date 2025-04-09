"""3019. Number of Changing Keys
Link: https://leetcode.com/problems/number-of-changing-keys/
Difficulty: Easy
Description: You are given a 0-indexed string s typed by a user. Changing a key is defined
as using a key different from the last used key. For example, s = "ab" has a change of a
key while s = "bBBb" does not have any.
Return the number of times the user had to change the key.
Note: Modifiers like shift or caps lock won't be counted in changing the key that is if
a user typed the letter 'a' and then the letter 'A' then it will not be considered as a
changing of key."""


class Solution:
    @staticmethod
    def countKeyChanges(s: str) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the number of key changes
        n = len(s)
        key_changes = 0
        s = s.lower()

        # Iterate through the string and count the number of key changes
        for i in range(1, n):
            if s[i] != s[i - 1]:
                key_changes += 1
        return key_changes


# Unit Test: s = "aAbBcC", Output = 2
assert Solution.countKeyChanges("aAbBcC") == 2

# Unit Test: s = "AaAaAaaA", Output = 0
assert Solution.countKeyChanges("AaAaAaaA") == 0

print("All unit tests are passed.")
