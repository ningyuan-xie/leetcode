# Link: https://leetcode.com/problems/repeated-substring-pattern/
# Difficulty: Easy
# Description: Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.

class Solution:
    # Optimal Solution: KMP Algorithm. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def repeatedSubstringPattern(s: str) -> bool:
        # Initialize the prefix table
        prefix_table = [0] * len(s)
        # Initialize the prefix length
        prefix_len = 0
        # Iterate through the range of 1 to the length of the string
        for i in range(1, len(s)):
            # If the characters match
            while prefix_len > 0 and s[i] != s[prefix_len]:
                prefix_len = prefix_table[prefix_len - 1]
            if s[i] == s[prefix_len]:
                prefix_len += 1
                prefix_table[i] = prefix_len
            else:
                prefix_table[i] = 0

        # Calculate the length of the longest proper prefix that is also a suffix
        prefix_len = prefix_table[-1]
        # Check if the string can be constructed by taking a substring of it
        # and appending multiple copies of the substring together
        return prefix_len > 0 and len(s) % (len(s) - prefix_len) == 0


# Unit Test: Input: s = "abab", Output: True
assert Solution.repeatedSubstringPattern("abab") is True

# Unit Test: Input: s = "aba", Output: False
assert Solution.repeatedSubstringPattern("aba") is False

# Unit Test: Input: s = "abcabcabcabc", Output: True
assert Solution.repeatedSubstringPattern("abcabcabcabc") is True

# Unit Test: Input: s = "abaababaab", Output: True
assert Solution.repeatedSubstringPattern("abaababaab") is True

print("All unit tests are passed")
