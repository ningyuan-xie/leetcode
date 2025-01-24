"""2490. Circular Sentence
Link: https://leetcode.com/problems/circular-sentence/
Difficulty: Easy
Description: A sentence is a list of words that are separated by a single space with no leading or
trailing spaces.
- For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters
are considered different.
A sentence is circular if:
- The last character of each word in the sentence is equal to the first character of its next word.
- The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular
sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not
circular sentences.
Given a string sentence, return true if it is circular. Otherwise, return false."""


class Solution:
    @staticmethod
    def isCircularSentence(sentence: str) -> bool:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        # Split the sentence into words
        words = sentence.split()  # E.g. ["leetcode", "exercises", "sound", "delightful"]

        # Check if each word's last character matches the next word's first character
        for i in range(len(words)):
            # Compare the last character of the current word with the first character of the next word
            if words[i][-1] != words[(i + 1) % len(words)][0]:
                return False
        return True


# Unit Test: sentence = "leetcode exercises sound delightful", Output: True
assert Solution.isCircularSentence("leetcode exercises sound delightful") is True

# Unit Test: sentence = "eetcode", Output: True
assert Solution.isCircularSentence("eetcode") is True

# Unit Test: sentence = "Leetcode is cool", Output: False
assert Solution.isCircularSentence("Leetcode is cool") is False

print("All unit tests are passed")
