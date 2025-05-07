"""520. Detect Capital
Link: https://leetcode.com/problems/detect-capital/
Difficulty: Easy
Description: We define the usage of capitals in a word to be right when one of the following cases holds:
• All letters in this word are capitals, like "USA".
• All letters in this word are not capitals, like "leetcode".
• Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right."""


class Solution:
    @staticmethod
    def detectCapitalUse(word: str) -> bool:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        return word == word.upper() or word == word.lower() or word == word.capitalize()


def unit_tests():
    # Input = "USA", Output = True
    assert Solution.detectCapitalUse("USA") is True

    # Input = "FlaG", Output = False
    assert Solution.detectCapitalUse("FlaG") is False

    # Input = "leetcode", Output = True
    assert Solution.detectCapitalUse("leetcode") is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
