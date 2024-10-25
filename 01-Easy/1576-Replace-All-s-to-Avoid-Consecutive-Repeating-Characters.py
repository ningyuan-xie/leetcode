"""1576. Replace All ?'s to Avoid Consecutive Repeating Characters
Link: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
Difficulty: Easy
Description: Given a string s containing only lowercase English letters and the '?' character,
convert all the '?' characters into lowercase letters such that the final string does not contain
any consecutive repeating characters. You cannot modify the non '?' characters.
It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
Return the final string after all the conversions (possibly zero) have been made. If there is more
than one solution, return any of them. It can be shown that an answer is always possible with the
given constraints."""


class Solution:
    @staticmethod
    def modifyString(s: str) -> str:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(n)"""
        # Convert the string into a list of characters
        s = list(s)  # E.g. "?zs" -> ['?', 'z', 's']

        # Replace '?' with a character that is not the same as the previous or next
        for i in range(len(s)):
            if s[i] == '?':
                # Initialize the previous and next characters
                prev_char = s[i - 1] if i > 0 else ''  # E.g. ['?', 'z', 's'] -> prev_char = ''
                next_char = s[i + 1] if i < len(s) - 1 else ''  # next_char = 'z'

                # Greedy Approach: Replace '?' with the FIRST character that is not the same as the
                # previous or next character
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char != prev_char and char != next_char:
                        s[i] = char  # E.g. ['?', 'z', 's'] -> ['a', 'z', 's']
                        break

        return ''.join(s)


# Unit Test: s = "?zs", Output: "azs"
assert Solution.modifyString("?zs") == "azs"

# Unit Test: s = "ubv?w", Output: "ubvaw"
assert Solution.modifyString("ubv?w") == "ubvaw"

# Unit Test: s = "j?qg??b", Output: "jaqgacb"
assert Solution.modifyString("j?qg??b") == "jaqgacb"

print("All unit tests are passed")
