"""1592. Rearrange Spaces Between Words
Link: https://leetcode.com/problems/rearrange-spaces-between-words/
Difficulty: Easy
Description: You are given a string text of words that are placed among some number of spaces.
Each word consists of one or more lowercase English letters and are separated by at least one space.
It's guaranteed that text contains at least one word.
Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words
and that number is maximized. If you cannot redistribute all the spaces equally, place the extra
spaces at the end, meaning the returned string should be the same length as text.
Return the string after rearranging the spaces."""


class Solution:
    @staticmethod
    def reorderSpaces(text: str) -> str:
        """Optimal Solution: Count Spaces and Words. Time Complexity: O(n), Space Complexity: O(n)"""
        # Count the number of spaces and words in the text
        space_count = text.count(' ')  # E.g. "  this   is  a sentence " -> 9
        words = text.split()  # "  this   is  a sentence " -> ['this', 'is', 'a', 'sentence']

        # Calculate the number of spaces between words and at the end of the text
        space_between_words = space_count // (len(words) - 1) if len(words) > 1 else 0  # 9 // 3 = 3
        space_at_end = space_count % (len(words) - 1) if len(words) > 1 else space_count  # 9 % 3 = 0

        # Construct the reordered text: join words with spaces between and at the end
        return (' ' * space_between_words).join(words) + ' ' * space_at_end


# Unit Test: text = "  this   is  a sentence ", Output: "this   is   a   sentence"
assert Solution.reorderSpaces("  this   is  a sentence ") == "this   is   a   sentence"

# Unit Test: text = " practice   makes   perfect", Output: "practice   makes   perfect "
assert Solution.reorderSpaces(" practice   makes   perfect") == "practice   makes   perfect "

# Unit Test: text = "hello", Output: "hello"
assert Solution.reorderSpaces("hello") == "hello"

print("All unit tests are passed.")
