"""1957. Delete Characters to Make Fancy String
Link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
Difficulty: Easy
Description: A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique."""


class Solution:
    @staticmethod
    def makeFancyString(s: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the result string as the first character
        result, count = s[0], 1

        # Iterate through the string
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  # Reset the count

            # Only add the character to the result if the count is less than 3
            if count < 3:
                result += s[i]

        return result


# Unit Test: s = "leeetcode", Output: "leetcode"
assert Solution.makeFancyString("leeetcode") == "leetcode"

# Unit Test: s = "aaabaaaa", Output: "aabaa"
assert Solution.makeFancyString("aaabaaaa") == "aabaa"

# Unit Test: s = "aab", Output: "aab"
assert Solution.makeFancyString("aab") == "aab"

print("All unit tests are passed.")
