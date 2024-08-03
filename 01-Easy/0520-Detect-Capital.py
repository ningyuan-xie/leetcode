"""520. Detect Capital
Link: https://leetcode.com/problems/detect-capital/
Difficulty: Easy
Description: Given a word, you need to judge whether the usage of capitals in it is right or not.
Given a string word, return true if the usage of capitals in it is right."""


class Solution:
    @staticmethod
    def detectCapitalUse(word: str) -> bool:
        """Optimal Solution: Count the number of capital letters in the word.
           Time Complexity: O(n), Space Complexity: O(1)"""
        # Count the number of capital letters in the word
        capital_count = sum(1 for char in word if char.isupper())
        # Return True if the word is all lowercase or all uppercase
        # or the first letter is uppercase and the rest are lowercase
        return (capital_count == 0
                or capital_count == len(word)
                or (capital_count == 1 and word[0].isupper()))


# Unit Test: Input = "USA", Output = True
assert Solution.detectCapitalUse("USA") == True

# Unit Test: Input = "FlaG", Output = False
assert Solution.detectCapitalUse("FlaG") == False

# Unit Test: Input = "leetcode", Output = True
assert Solution.detectCapitalUse("leetcode") == True

print("All unit tests are passed")
