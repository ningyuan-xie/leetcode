"""3083. Existence of a Substring in a String and Its Reverse
Link: https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/
Difficulty: Easy
Description: Given a string s, find any substring of length 2 which is also present in the
reverse of s.
Return true if such a substring exists, and false otherwise."""


class Solution:
    @staticmethod
    def isSubstringPresent(s: str) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)"""
        # Base case: If the string is empty, then return False
        if not s:
            return False

        s_reverse = s[::-1]
        # Iterate through the string and check if any substring of length 2 is present in the reverse
        for i in range(len(s) - 1):
            if s[i:i + 2] in s_reverse:
                return True

        return False


# Unit Test: s = "leetcode", Output = True
assert Solution.isSubstringPresent("leetcode") is True

# Unit Test: s = "abcba", Output = True
assert Solution.isSubstringPresent("abcba") is True

# Unit Test: s = "abcd", Output = False
assert Solution.isSubstringPresent("abcd") is False

print("All unit tests are passed")
