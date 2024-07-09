# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Difficulty: Easy
# Description: Write a function that takes a string as input and reverse only the vowels of a string.

class Solution:
    # Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)
    # Similar to 0344-Reverse-String.py
    @staticmethod
    def reverseVowels(s: str) -> str:
        # Initialize a set of vowels
        vowels = set("aeiouAEIOU")
        # Convert the string into a list of characters
        s = list(s)  # "hello" -> ["h", "e", "l", "l", "o"]
        # Initialize two pointers: left and right
        left, right = 0, len(s) - 1
        # Loop until left pointer is less than right pointer
        while left < right:
            # If the character at the left pointer is not a vowel, move the left pointer to the right
            if s[left] not in vowels:
                left += 1
            # If the character at the right pointer is not a vowel, move the right pointer to the left
            elif s[right] not in vowels:
                right -= 1
            # If both characters at the left and right pointers are vowels, swap them
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        # Convert the list of characters back into a string
        return "".join(s)


# Unit Test: Input: s = "hello", Output: "holle"
assert Solution.reverseVowels("hello") == "holle"

# Unit Test: Input: s = "leetcode", Output: "leotcede"
assert Solution.reverseVowels("leetcode") == "leotcede"

# Unit Test: Input: s = "aA", Output: "Aa"
assert Solution.reverseVowels("aA") == "Aa"

print("All unit tests are passed")
