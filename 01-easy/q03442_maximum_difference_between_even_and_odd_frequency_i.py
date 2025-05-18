"""3442. Maximum Difference Between Even and Odd Frequency I
Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
Difficulty: Easy
Description: You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:
• One of the characters has an even frequency in the string.
• The other character has an odd frequency in the string.
Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency."""


class Solution:
    @staticmethod
    def maxDifference(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        even_freq = float('inf')
        odd_freq = float('-inf')

        for count in freq.values():
            if count % 2 == 0:
                even_freq = min(even_freq, count)
            else:
                odd_freq = max(odd_freq, count)

        return odd_freq - even_freq if odd_freq != float('-inf') and even_freq != float('inf') else 0


def unit_tests():
    # Input: s = "aaaaabbc", Output: 3
    assert Solution.maxDifference("aaaaabbc") == 3

    # Input: s = "abcabcab", Output: 1
    assert Solution.maxDifference("abcabcab") == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
