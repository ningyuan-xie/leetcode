"""1935. Maximum Number of Words You Can Type
Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/
Difficulty: Easy
Description: There is a malfunctioning keyboard where some letter keys do not work. All other keys
on the keyboard work properly.
Given a string text of words separated by a single space (no leading or trailing spaces) and a
string brokenLetters of all distinct letter keys that are broken, return the number of words in
text you can fully type using this keyboard."""


class Solution:
    @staticmethod
    def canBeTypedWords(text: str, brokenLetters: str) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)"""
        # Convert brokenLetters to a set
        broken = set(brokenLetters)  # E.g., "ad" -> {"a", "d"}
        words = text.split()
        count = 0

        for word in words:
            for letter in word:
                if letter in broken:
                    break
            else:
                count += 1

        return count


# Unit Test: text = "hello world", brokenLetters = "ad", Output: 1
assert Solution.canBeTypedWords("hello world", "ad") == 1

# Unit Test: text = "leet code", brokenLetters = "lt", Output: 1
assert Solution.canBeTypedWords("leet code", "lt") == 1

# Unit Test: text = "leet code", brokenLetters = "e", Output: 0
assert Solution.canBeTypedWords("leet code", "e") == 0

print("All unit tests are passed.")
