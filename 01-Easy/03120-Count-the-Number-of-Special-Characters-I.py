"""3120. Count the Number of Special Characters I
Link: https://leetcode.com/problems/count-the-number-of-special-characters-i
Difficulty: Easy
Description: You are given a string word. A letter is called special if it appears both in
lowercase and uppercase in word.
Return the number of special letters in word."""


class Solution:
    @staticmethod
    def numberOfSpecialChars(word: str) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)"""
        count = 0

        # Remove duplicate characters from the word
        word = list(set(word))  # ['c', 'b', 'C', 'a', 'A', 'B']
        for char in word:
            # If the character is lower, check if the upper case is also present
            if char.islower() and char.upper() in word:
                count += 1
        return count


# Unit Test: word = "aaAbcBC", Output = 3
assert Solution.numberOfSpecialChars("aaAbcBC") == 3

# Unit Test: word = "abc", Output = 0
assert Solution.numberOfSpecialChars("abc") == 0

# Unit Test: word = "abBCab", Output = 1
assert Solution.numberOfSpecialChars("abBCab") == 1

print("All unit tests are passed.")
