"""9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Description: Given an integer x, return true if x is palindrome integer.
Follow up: Could you solve it without converting the integer to a string?"""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        """Optimal Solution: Reverse Half. Time Complexity: O(log10(n)), Space Complexity: O(1)."""
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            # Append the last digit to the reversed half
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10
        
        # For even digit length: x == reversed_half
        # For odd digit length: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
        

def unit_tests():
    # Input: x = 121, Output: True
    assert Solution.isPalindrome(121) is True

    # Input: x = -121, Output: False
    assert Solution.isPalindrome(-121) is False

    # Input: x = 10, Output: False
    assert Solution.isPalindrome(10) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
