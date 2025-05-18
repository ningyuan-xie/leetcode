"""409. Longest Palindrome
Link: https://leetcode.com/problems/longest-palindrome/
Difficulty: Easy
Description: Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome."""


class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Create a dictionary to count occurrences of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Initialize length of longest palindrome
        length = 0
        odd_found = False

        # Iterate through the character counts
        for count in char_count.values():
            # Add the largest even number less than or equal to count
            length += count // 2 * 2
            # Check if there is an odd count
            if count % 2 == 1:
                odd_found = True

        # If there is at least one odd count, we can add one more character to the palindrome
        if odd_found:
            length += 1

        return length


def unit_tests():
    # Input: s = "abccccdd", Output: 7
    assert Solution.longestPalindrome("abccccdd") == 7

    # Input: s = "a", Output: 1
    assert Solution.longestPalindrome("a") == 1

    # Input: s = "bb", Output: 2
    assert Solution.longestPalindrome("bb") == 2


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
