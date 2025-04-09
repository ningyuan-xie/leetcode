"""1078. Occurrences After Bigram
Link: https://leetcode.com/problems/occurrences-after-bigram/
Difficulty: Easy
Description: Given two strings first and second, consider occurrences in some text of the form
"first second third", where second comes immediately after first, and third comes immediately
after second.
Return an array of all the words third for each occurrence of "first second third"."""

from typing import List


class Solution:
    @staticmethod
    def findOcurrences(text: str, first: str, second: str) -> List[str]:
        """Optimal Solution: One Pass. Time Complexity: O(n), Space Complexity: O(n)."""
        words = text.split()
        n, result = len(words), []

        for i in range(2, n):
            if words[i - 2] == first and words[i - 1] == second:
                result.append(words[i])

        return result


# Unit Test: text = "alice is a good girl she is a good student", first = "a", second = "good",
# Output: ["girl", "student"]
assert Solution.findOcurrences("alice is a good girl she is a good student",
                               "a", "good") == ["girl", "student"]

# Unit Test: text = "we will we will rock you", first = "we", second = "will", Output: ["we","rock"]
assert Solution.findOcurrences("we will we will rock you",
                               "we", "will") == ["we", "rock"]

print("All unit tests are passed.")
