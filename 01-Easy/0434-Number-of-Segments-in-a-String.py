# Link: https://leetcode.com/problems/number-of-segments-in-a-string/
# Difficulty: Easy
# Description: You are given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

class Solution:
    # Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def countSegments(s: str) -> int:
        # Initialize the count of segments
        count = 0
        # Iterate through the string
        for i in range(len(s)):
            # If the current character is not a space
            # and the previous character is a space or the first character
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                count += 1
        return count


# Unit Test: Input: s = "Hello, my name is John", Output: 5
assert Solution.countSegments("Hello, my name is John") == 5

# Unit Test: Input: s = "Hello", Output: 1
assert Solution.countSegments("Hello") == 1

# Unit Test: Input: s = "love live! mu'sic forever", Output: 4
assert Solution.countSegments("love live! mu'sic forever") == 4

print("All unit tests are passed")
