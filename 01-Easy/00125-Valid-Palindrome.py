"""125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""


class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize two pointers
        left, right = 0, len(s) - 1

        # Check if the string s is a palindrome
        while left < right:
            # Skip all the non-alphanumeric characters
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

        
def unit_tests():
    # Input: s = "A man, a plan, a canal: Panama", Output: True
    assert Solution.isPalindrome("A man, a plan, a canal: Panama") is True

    # Input: s = "race a car", Output: False
    assert Solution.isPalindrome("race a car") is False

    # Input: s = "a", Output: True
    assert Solution.isPalindrome("a") is True

    # Input: s = "ab", Output: False
    assert Solution.isPalindrome("ab") is False

    # Input: s = "a.", Output: True
    assert Solution.isPalindrome("a.") is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
