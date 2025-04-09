"""2000. Reverse Prefix of Word
Link: https://leetcode.com/problems/reverse-prefix-of-word/
Difficulty: Easy
Description: Given a 0-indexed string word and a character ch, reverse the segment of word that
starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character
ch does not exist in word, do nothing.
- For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at
0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string."""


class Solution:
    @staticmethod
    def reversePrefix(word: str, ch: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)"""
        # Find the first occurrence of the target character
        index = word.find(ch)

        # If the character is found, reverse the prefix and concatenate with the rest
        if index != -1:
            return word[:index + 1][::-1] + word[index + 1:]

        # If the character is not found, return the original word
        return word


# Unit Test: word = "abcdefd", ch = "d", Output: "dcbaefd"
assert Solution.reversePrefix("abcdefd", "d") == "dcbaefd"

# Unit Test: word = "xyxzxe", ch = "z", Output: "zxyxxe"
assert Solution.reversePrefix("xyxzxe", "z") == "zxyxxe"

# Unit Test: word = "abcd", ch = "z", Output: "abcd"
assert Solution.reversePrefix("abcd", "z") == "abcd"

print("All unit tests are passed")
