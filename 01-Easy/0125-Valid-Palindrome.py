# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Description: Given a string s, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.

class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        # Convert the string to lowercase and remove non-alphanumeric characters
        # isalnum() checks if the character is an alphabet or a digit: a-z, A-Z, 0-9
        # ''.join([]) concatenates list of str into str without spaces
        s = ''.join([char.lower() for char in s if char.isalnum()])
        # Check if the string is a palindrome
        return s == s[::-1]


# Unit Test: Input: s = "A man, a plan, a canal: Panama", Output: True
assert Solution.isPalindrome("A man, a plan, a canal: Panama") == True

# Unit Test: Input: s = "race a car", Output: False
assert Solution.isPalindrome("race a car") == False

# Unit Test: Input: s = "a", Output: True
assert Solution.isPalindrome("a") == True

# Unit Test: Input: s = "ab", Output: False
assert Solution.isPalindrome("ab") == False

# Unit Test: Input: s = "a.", Output: True
assert Solution.isPalindrome("a.") == True

print("All unit tests are passed")
