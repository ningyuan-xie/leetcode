"""2309. Greatest English Letter in Upper and Lower Case
Link: https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
Difficulty: Easy
Description: Given a string of English letters s, return the greatest English letter which occurs as
both a lowercase and uppercase letter in s. The returned letter should be in uppercase.
If no such letter exists, return an empty string.
An English letter b is greater than another letter a if b appears after a in the English alphabet."""


class Solution:
    @staticmethod
    def greatestLetter(s: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize a set to store the lowercase letters
        lower_case = set()

        # Iterate through the string
        for char in s:
            if char.islower():
                lower_case.add(char)

        # Iterate through the string again to find the greatest letter
        greatest_letter = ""
        for char in s:
            if char.isupper() and char.lower() in lower_case:
                if greatest_letter < char:
                    greatest_letter = char

        return greatest_letter


# Unit Test: s = "lEeTcOdE", Output: "E"
assert Solution.greatestLetter("lEeTcOdE") == "E"

# Unit Test: s = "arRAzFif", Output: "R"
assert Solution.greatestLetter("arRAzFif") == "R"

# Unit Test: s = "AbCdEfGhIjK", Output: ""
assert Solution.greatestLetter("AbCdEfGhIjK") == ""

print("All unit tests are passed.")
