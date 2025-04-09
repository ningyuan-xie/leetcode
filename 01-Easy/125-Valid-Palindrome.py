"""125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Description: Given a string s, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases."""


class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        """Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(n)"""
        # Convert the string to lowercase and remove non-alphanumeric characters
        # isalnum() checks if the character is an alphabet or a digit: a-z, A-Z, 0-9
        # ''.join([]) concatenates list of str into str without spaces
        s = ''.join([char.lower() for char in s if char.isalnum()])
        # Check if the string is a palindrome
        return s == s[::-1]

    @staticmethod
    def isPalindromeTwoPointers(s: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the two pointers
        left, right = 0, len(s) - 1

        # Check if the string s is a palindrome
        while left < right:
            # Skip all the non-alphanumeric characters and go to the next while loop
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            # Check if the left and right characters are equal
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


# Unit Test: Input: s = "A man, a plan, a canal: Panama", Output: True
assert Solution.isPalindrome("A man, a plan, a canal: Panama") is True

# Unit Test: Input: s = "race a car", Output: False
assert Solution.isPalindromeTwoPointers("race a car") is False

# Unit Test: Input: s = "a", Output: True
assert Solution.isPalindrome("a") is True

# Unit Test: Input: s = "ab", Output: False
assert Solution.isPalindromeTwoPointers("ab") is False

# Unit Test: Input: s = "a.", Output: True
assert Solution.isPalindrome("a.") is True

print("All unit tests are passed")
