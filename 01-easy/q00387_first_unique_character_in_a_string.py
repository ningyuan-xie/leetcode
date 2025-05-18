"""387. First Unique Character in a String
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Difficulty: Easy
Description: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1."""


class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Create a dictionary to count occurrences of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Iterate through the string to find the first unique character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return -1


def unit_tests():
    # Input: s = "leetcode", Output: 0
    assert Solution.firstUniqChar("leetcode") == 0

    # Input: s = "loveleetcode", Output: 2
    assert Solution.firstUniqChar("loveleetcode") == 2

    # Input: s = "aabb", Output: -1
    assert Solution.firstUniqChar("aabb") == -1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
