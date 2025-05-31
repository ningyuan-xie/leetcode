"""819. Most Common Word
Link: https://leetcode.com/problems/most-common-word/
Difficulty: Easy
Description: Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.
Note that words can not contain punctuation symbols."""

from typing import List


class Solution:
    @staticmethod
    def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Convert paragraph to lowercase and replace non-alphanumeric chars with spaces
        normalized = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized.split()
        
        # Count word frequencies, excluding banned words
        banned_set = set(banned)
        word_count = {}
        for word in words:
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1
        
        # Find the word with maximum frequency
        return max(word_count.items(), key=lambda x: x[1])[0]


def unit_tests():
    # Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"], Output: "ball"
    assert Solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball"

    # Input: paragraph = "a.", banned = [], Output: "a"
    assert Solution.mostCommonWord("a.", []) == "a"

    # Input: paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"], Output: "b"
    assert Solution.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]) == "b"

    # Input: paragraph = "Bob. hIt, baLl", banned = ["bob", "hit"], Output: "ball"
    assert Solution.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]) == "ball"


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")
