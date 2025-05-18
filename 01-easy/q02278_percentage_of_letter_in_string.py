"""2278. Percentage of Letter in String
Link: https://leetcode.com/problems/percentage-of-letter-in-string/
Difficulty: Easy
Description: Given a string s and a character letter, return the percentage of characters in s that
equal letter rounded down to the nearest whole percent."""


class Solution:
    @staticmethod
    def percentageLetter(s: str, letter: str) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the count of the specific letter
        count_letter = 0

        # Iterate through the string
        for char in s:
            # Check if the current character is the specific letter
            if char == letter:
                count_letter += 1

        # Calculate the percentage of the specific letter
        percentage = (count_letter / len(s)) * 100

        return int(percentage)


# Unit Test: s = "foobar", letter = "o", Output: 33
assert Solution.percentageLetter("foobar", "o") == 33

# Unit Test: s = "jjjj", letter = "k", Output: 0
assert Solution.percentageLetter("jjjj", "k") == 0

print("All unit tests are passed.")
