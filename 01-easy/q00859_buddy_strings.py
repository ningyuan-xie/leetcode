"""859. Buddy Strings
Link: https://leetcode.com/problems/buddy-strings/
Difficulty: Easy
Description: Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
• For example, swapping at indices 0 and 2 in "abcd" results in "cbad"."""


class Solution:
    @staticmethod
    def buddyStrings(s: str, goal: str) -> bool:
        """Optimal Solution: String Iteration with zip(). Time Complexity: O(n), Space Complexity: O(1)."""
        # Check if the two strings have the same length
        if len(s) != len(goal):
            return False

        # Check if the two strings are equal
        if s == goal:
            # Check if there are at least two identical characters to swap in the string
            return len(set(s)) < len(s)

        # Find the two characters that are different
        diff = [(x, y) for x, y in zip(s, goal) if x != y]
        # Check if there are exactly two different characters, and the two characters can be swapped to make the two strings equal, such as [(a, b), (b, a)]
        return len(diff) == 2 and diff[0] == diff[1][::-1]


def unit_tests():
    # Input: a = "ab", b = "ba", Output: True
    assert Solution.buddyStrings("ab", "ba") is True

    # Input: a = "ab", b = "ab", Output: False
    assert Solution.buddyStrings("ab", "ab") is False

    # Input: a = "aa", b = "aa", Output: True
    assert Solution.buddyStrings("aa", "aa") is True

    # Input: a = "aaaaaaabc", b = "aaaaaaacb", Output: True
    assert Solution.buddyStrings("aaaaaaabc", "aaaaaaacb") is True

    # Input: a = "", b = "aa", Output: False
    assert Solution.buddyStrings("", "aa") is False

    # Input: a = "abcaa", b = "abcbb", Output: False
    assert Solution.buddyStrings("abcaa", "abcbb") is False


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")
