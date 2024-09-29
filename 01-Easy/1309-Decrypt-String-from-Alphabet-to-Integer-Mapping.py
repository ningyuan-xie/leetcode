"""1309. Decrypt String from Alphabet to Integer Mapping
Link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
Difficulty: Easy
Description: You are given a string s formed by digits and '#'. We want to map s to English lowercase
characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.
The test cases are generated so that a unique mapping will always exist."""


class Solution:
    @staticmethod
    def freqAlphabets(s: str) -> str:
        """Optimal Solution: Reverse Iteration. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the result
        result = ""

        # Traverse the string in reverse order
        i = len(s) - 1
        while i >= 0:
            # If the current character is '#', then extract the two digits
            if s[i] == '#':
                result = chr(int(s[i - 2:i]) + 96) + result  # + 96 to convert num to lowercase letter
                i -= 3
            # Otherwise, extract the single digit
            else:
                result = chr(int(s[i]) + 96) + result
                i -= 1

        return result


# Unit Test: s = "10#11#12", Output: "jkab"
assert Solution.freqAlphabets("10#11#12") == "jkab"

# Unit Test: s = "1326#", Output: "acz"
assert Solution.freqAlphabets("1326#") == "acz"

# Unit Test: s = "25#", Output: "y"
assert Solution.freqAlphabets("25#") == "y"

print("All unit tests are passed")
