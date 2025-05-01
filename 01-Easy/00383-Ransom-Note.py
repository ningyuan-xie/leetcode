"""383. Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Difficulty: Easy
Description: Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote."""


class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n + m), Space Complexity: O(n).
        Similar to 350. Intersection of Two Arrays II."""
        # Create a dictionary to count occurrences of each character in magazine
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1

        # Check if ransomNote can be constructed from magazine
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        return True


def unit_tests():
    # Input: ransomNote = "a", magazine = "b", Output: False
    assert Solution.canConstruct("a", "b") is False

    # Input: ransomNote = "aa", magazine = "ab", Output: False
    assert Solution.canConstruct("aa", "ab") is False

    # Input: ransomNote = "aa", magazine = "aab", Output: True
    assert Solution.canConstruct("aa", "aab") is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
