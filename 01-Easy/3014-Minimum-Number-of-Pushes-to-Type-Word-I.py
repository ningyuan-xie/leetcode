"""3014. Minimum Number of Pushes to Type Word I
Link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word/
Difficulty: Easy
Description: You are given a string word containing distinct lowercase English letters.
Telephone keypads have keys mapped with distinct collections of lowercase English letters,
which can be used to form words by pushing them. For example, the key 2 is mapped with
["a","b","c"], we need to push the key one time to type "a", two times to type "b", and
three times to type "c" .
It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The
keys can be remapped to any amount of letters, but each letter must be mapped to exactly
one key. You need to find the minimum number of times the keys will be pushed to type the
string word.
Return the minimum number of pushes needed to type word after remapping the keys.
An example mapping of letters to keys on a telephone keypad is given below. Note that
1, *, #, and 0 do not map to any letters."""


class Solution:
    @staticmethod
    def minimumPushes(word: str) -> int:
        """Optimal Solution: While Loop. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the total number of words and pushes
        n = len(word)
        push = 0

        # Iterate through the word and add additional pushes for each round
        word_count = 0
        additional_push = 0
        while n:
            word_count += 1
            # Whenever a new round starts, add one additional push going forward
            if word_count == 9:
                additional_push += 1
                # Reset the word count back to 1
                word_count = 1
            push += 1 + additional_push
            n -= 1

        return push


# Unit Test: word = "abcde", Output = 5
assert Solution.minimumPushes("abcde") == 5

# Unit Test: word = "xycdefghij", Output = 12
assert Solution.minimumPushes("xycdefghij") == 12

print("All unit tests are passed")
