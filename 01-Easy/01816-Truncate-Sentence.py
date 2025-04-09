"""1816. Truncate Sentence
Link: https://leetcode.com/problems/truncate-sentence/
Difficulty: Easy
Description: A sentence is a list of words that are separated by a single space with no leading or
trailing spaces. Each of the words consists of only uppercase and lowercase English letters
(no punctuation).
- For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s and an integer k. You want to truncate s such that it contains only the
first k words. Return s after truncating it."""


class Solution:
    @staticmethod
    def truncateSentence(s: str, k: int) -> str:
        """Optimal Solution: Split and Join. Time Complexity: O(n), Space Complexity: O(n)"""
        # Split the sentence into words
        words = s.split()

        # Return the first k words as a sentence
        return " ".join(words[:k])


# Unit Test: s = "Hello how are you Contestant", k = 4, Output: "Hello how are you"
assert Solution.truncateSentence("Hello how are you Contestant", 4) == "Hello how are you"

# Unit Test: s = "What is the solution to this problem", k = 4, Output: "What is the solution"
assert (Solution.truncateSentence("What is the solution to this problem", 4)
        == "What is the solution")

# Unit Test: s = "chopper is not a tanuki", k = 5, Output: "chopper is not a tanuki"
assert Solution.truncateSentence("chopper is not a tanuki", 5) == "chopper is not a tanuki"

print("All unit tests are passed")
