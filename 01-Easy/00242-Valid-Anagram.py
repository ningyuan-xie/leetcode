"""242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        # Base case
        if len(s) != len(t):
            return False

        # Count characters in s
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Decrease the count for each character in t
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True


def unit_tests():
    # Input: s = "anagram", t = "nagaram"
    assert Solution.isAnagram("anagram", "nagaram") is True

    # Input: s = "rat", t = "car"
    assert Solution.isAnagram("rat", "car") is False

    # Input: s = "a", t = "ab"
    assert Solution.isAnagram("a", "ab") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
