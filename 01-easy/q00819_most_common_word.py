"""819. Most Common Word
Link: https://leetcode.com/problems/most-common-word/
Difficulty: Easy
Description: Given a string paragraph and a string array of the banned words banned, return the most
frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and
that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase."""

from typing import List


class Solution:
    @staticmethod
    def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        """ Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Normalize the paragraph: Convert to lowercase and replace punctuations with spaces
        normalized_str = ''
        for char in paragraph:
            if char.isalnum():  # Check if the character is alphanumeric
                normalized_str += char.lower()
            else:
                normalized_str += ' '  # Replace punctuations with spaces
        # Split the string into a list of words
        words = normalized_str.split()  # E.g. "Bob hit a ball" -> ["bob", "hit", "a", "ball"]

        # Initialize a dictionary to count frequencies of each word
        word_count = {}
        # Populate the dictionary with word counts, ignoring banned words
        banned_set = set(banned)  # Convert the banned list to a set for O(1) lookups
        for word in words:
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1

        # Find the most common word (max frequency)
        most_common_word, max_count = '', 0
        for (word, count) in word_count.items():  # .items() is key-value pair: ("bob", 1)
            if count > max_count:
                most_common_word, max_count = word, count

        return most_common_word


# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
# banned = ["hit"], Output: "ball"
assert Solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
                               ["hit"]) == "ball"

# Input: paragraph = "a.", banned = [], Output: "a"
assert Solution.mostCommonWord("a.", []) == "a"

# Input: paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"], Output: "b"
assert Solution.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]) == "b"

# Input: paragraph = "Bob. hIt, baLl", banned = ["bob", "hit"], Output: "ball"
assert Solution.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]) == "ball"

print("All unit tests are passed.")
