"""1704. Determine if String Halves Are Alike
Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/
Difficulty: Easy
Description: You are given a string s of even length. Split this string into two halves of equal
lengths, and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I',
'O', 'U'). Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false."""


class Solution:
    @staticmethod
    def halves_are_alike(s: str) -> bool:
        """Optimal Solution: Count Vowels. Time Complexity: O(n), Space Complexity: O(1)"""
        # Define a set of vowels
        vowels = set("aeiouAEIOU")

        # Initialize counters for the first and second halves
        count_a = count_b = 0

        # Traverse the string and count vowels in the first and second halves
        for i in range(len(s)):
            if s[i] in vowels:
                if i < len(s) // 2:
                    count_a += 1
                else:
                    count_b += 1

        # Return True if the counts are equal, False otherwise
        return count_a == count_b


# Unit Test: s = "book", Output: True
assert Solution.halves_are_alike("book") is True

# Unit Test: s = "textbook", Output: False
assert Solution.halves_are_alike("textbook") is False

# Unit Test: s = "MerryChristmas", Output: False
assert Solution.halves_are_alike("MerryChristmas") is False

# Unit Test: s = "AbCdEfGh", Output: True
assert Solution.halves_are_alike("AbCdEfGh") is True

print("All unit tests are passed")
