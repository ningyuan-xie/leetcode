"""1668. Maximum Repeating Substring
Link: https://leetcode.com/problems/maximum-repeating-substring/
Difficulty: Easy
Description: For a string sequence, a string word is k-repeating if word concatenated k times is a
substring of sequence. The word's maximum k-repeating value is the highest value k where word is
k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value
is 0.
Given strings sequence and word, return the maximum k-repeating value of word in sequence."""


class Solution:
    @staticmethod
    def max_repeating(sequence: str, word: str) -> int:
        """Optimal Solution: Incremental Search. Time Complexity: O(n * m), Space Complexity: O(n)"""
        count = 0
        repeated_word = word

        # Keep appending word to itself until repeated_word is no longer in sequence
        while repeated_word in sequence:
            count += 1  # The final return value
            repeated_word += word  # Increase the repetition by one more word for next loop
        return count


# Unit Test: sequence = "ababc", word = "ab", Output: 2
assert Solution.max_repeating("ababc", "ab") == 2

# Unit Test: sequence = "ababc", word = "ba", Output: 1
assert Solution.max_repeating("ababc", "ba") == 1

# Unit Test: sequence = "ababc", word = "ac", Output: 0
assert Solution.max_repeating("ababc", "ac") == 0

# Unit Test: sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba", word = "aaaba", Output: 5
assert Solution.max_repeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba") == 5

print("All unit tests are passed")
