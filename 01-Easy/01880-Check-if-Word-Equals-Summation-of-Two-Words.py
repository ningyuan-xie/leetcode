"""1880. Check if Word Equals Summation of Two Words
Link: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
Difficulty: Easy
Description: The letter value of a letter is its position in the alphabet starting from 0
(i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
The numerical value of some string of lowercase English letters s is the concatenation of the
letter values of each letter in s, which is then converted into an integer.
For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After
converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase
English letters 'a' through 'j' inclusive.
Return true if the summation of the numerical values of firstWord and secondWord equals the
numerical value of targetWord, or false otherwise."""


class Solution:
    @staticmethod
    def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
        """Optimal Solution: Convert String and Sum. Time Complexity: O(n), Space Complexity: O(1)"""

        def get_numerical_value(word: str) -> int:
            """Helper function to convert a word to its numerical value.
               E.g. "acb" -> "021" -> 21"""
            return int("".join(str(ord(char) - ord("a"))
                               for char in word))

        return (get_numerical_value(firstWord) + get_numerical_value(secondWord)
                == get_numerical_value(targetWord))


# Unit Test: firstWord = "acb", secondWord = "cba", targetWord = "cdb", Output: True
assert Solution.isSumEqual("acb", "cba", "cdb") is True

# Unit Test: firstWord = "aaa", secondWord = "a", targetWord = "aab", Output: False
assert Solution.isSumEqual("aaa", "a", "aab") is False

print("All unit tests are passed.")
