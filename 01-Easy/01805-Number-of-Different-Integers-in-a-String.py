"""1805. Number of Different Integers in a String
Link: https://leetcode.com/problems/number-of-different-integers-in-a-string/
Difficulty: Easy
Description: You are given a string word that consists of digits and lowercase English letters.
You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become
" 123  34 8  34". Notice that you are left with some integers that are separated by at least one
space: "123", "34", "8", and "34".
Return the number of different integers after performing the replacement operations on word.
Two integers are considered different if their decimal representations without any leading zeros
are different."""


class Solution:
    @staticmethod
    def num_different_integers(word: str) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a set to store unique integers
        integers = set()

        # Replace non-digit characters with spaces
        for char in word:
            if not char.isdigit():
                word = word.replace(char, " ")

        # Add integers to the set
        for num in word.split():  # E.g. " 123  34 8  34" -> ["123", "34", "8", "34"]
            integers.add(int(num))  # E.g. ["123", "34", "8", "34"] -> {123, 34, 8}

        return len(integers)


# Unit Test: word = "a123bc34d8ef34", Output: 3
assert Solution.num_different_integers("a123bc34d8ef34") == 3

# Unit Test: word = "leet1234code234", Output: 2
assert Solution.num_different_integers("leet1234code234") == 2

# Unit Test: word = "a1b01c001", Output: 1
assert Solution.num_different_integers("a1b01c001") == 1

print("All unit tests are passed.")
