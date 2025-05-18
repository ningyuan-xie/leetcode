"""680. Valid Palindrome II
Link: https://leetcode.com/problems/valid-palindrome-ii/
Difficulty: Easy
Description: Given a string s, return true if the s can be palindrome after deleting at most one character from it."""


class Solution:
    @staticmethod
    def validPalindrome(s: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        
        def is_palindrome(l: int, r: int) -> bool:
            """Helper function to check palindrome between given indices."""
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Check both possible deletions (left+1 or right-1)
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
            
        return True


def unit_tests():
    # Input: s = "aba", Output: True
    assert Solution.validPalindrome("aba") is True

    # Input: s = "abca", Output: True
    assert Solution.validPalindrome("abca") is True

    # Input: s = "abc", Output: False
    assert Solution.validPalindrome("abc") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
