"""2042. Check if Numbers Are Ascending in a Sentence
Link: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence
Difficulty: Easy
Description: A sentence is a list of tokens separated by a single space with no leading or trailing
spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or
a word consisting of lowercase English letters.
- For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are
numbers and the other tokens such as "puppy" are words.
Given a string s representing a sentence, you need to check if all the numbers in s are strictly
increasing from left to right (i.e., other than the last number, each number is strictly smaller
than the number on its right in s).
Return true if so, or false otherwise."""


class Solution:
    @staticmethod
    def areNumbersAscending(s: str) -> bool:
        """Optimal Solution: Split and Check. Time Complexity: O(n), Space Complexity: O(n)."""
        # Split the sentence into words
        words = s.split()

        # Initialize the previous number (minimum number is 0)
        prev = 0

        # Traverse each word in the sentence
        for word in words:
            # Check if the word is a number
            if word.isnumeric():
                # Convert the word to an integer
                num = int(word)

                # Check if the number is not ascending
                if num <= prev:
                    return False

                # Update the previous number
                prev = num

        return True


# Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles", Output: True
assert Solution.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles") is True

# Input: s = "hello world 5 x 5", Output: False
assert Solution.areNumbersAscending("hello world 5 x 5") is False

# Input: s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s", Output: False
assert Solution.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 "
                                    "and 60 s") is False

print("All unit tests are passed.")
