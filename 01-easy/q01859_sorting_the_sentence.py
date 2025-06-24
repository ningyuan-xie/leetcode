"""1859. Sorting the Sentence
Link: https://leetcode.com/problems/sorting-the-sentence/
Difficulty: Easy
Description: A sentence is a list of words that are separated by a single space with no leading or
trailing spaces. Each word consists of lowercase and uppercase English letters.
A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging
the words in the sentence.
- For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or
"is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original
sentence."""


class Solution:
    @staticmethod
    def sortSentence(s: str) -> str:
        """Optimal Solution: Sort the shuffled sentence based on the numbers at the end of each word.
           Time Complexity: O(n), Space Complexity: O(n)."""
        # Split the input sentence into words
        # E.g. "is2 sentence4 This1 a3" -> ["is2", "sentence4", "This1", "a3"]
        words = s.split()

        # Sort the words based on the trailing number
        # E.g. ["is2", "sentence4", "This1", "a3"] -> ["This1", "is2", "a3", "sentence4"]
        sorted_words = sorted(words, key=lambda word: int(word[-1]))

        # Remove the trailing number and join the words
        sorted_sentence = " ".join(word[:-1] for word in sorted_words)

        return sorted_sentence


# Input: s = "is2 sentence4 This1 a3", Output: "This is a sentence"
assert Solution.sortSentence("is2 sentence4 This1 a3") == "This is a sentence"

# Input: s = "Myself 2 Me1 I4 and3", Output: "Me Myself and I"
assert Solution.sortSentence("Myself2 Me1 I4 and3") == "Me Myself and I"

print("All unit tests are passed.")
