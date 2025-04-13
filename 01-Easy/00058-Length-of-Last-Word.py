"""58. Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy
Description: Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only."""


class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Split the string into words using whitespace as the delimiter
        words = s.split()
        # Return the length of the last word
        return len(words[-1]) if words else 0


def unit_tests():
    # Input: s = "Hello World", Output: 5
    assert Solution.lengthOfLastWord("Hello World") == 5

    # Input: s = "   fly me to   the moon  ", Output: 4
    assert Solution.lengthOfLastWord("   fly me to   the moon  ") == 4

    # Input: s = "luffy is still joyboy", Output: 6
    assert Solution.lengthOfLastWord("luffy is still joyboy") == 6

    # Input: s = "a", Output: 1
    assert Solution.lengthOfLastWord("a") == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
