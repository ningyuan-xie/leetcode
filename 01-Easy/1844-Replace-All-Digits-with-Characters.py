"""1844. Replace All Digits with Characters
Link: https://leetcode.com/problems/replace-all-digits-with-characters/
Difficulty: Easy
Description: You are given a 0-indexed string s that has lowercase English letters in its even
indices and digits in its odd indices.
You must perform an operation shift(c, x), where c is a character and x is a digit, that returns
the xth character after c.
For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with the result of the shift(s[i-1], s[i])
operation.
Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
Note that shift(c, x) is not a preloaded function, but an operation to be implemented as part of
the solution."""


class Solution:
    @staticmethod
    def replaceDigits(s: str) -> str:
        """Optimal Solution: Digit Shift. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the result
        result = []

        # Iterate through the string
        for i in range(len(s)):
            # If the index is odd: 1, 3, 5, ...
            if i % 2 == 1:
                # Shift the character by the digit: ord('a') + 1 = ord('b'); chr(ord('b')) = 'b'
                result.append(chr(ord(s[i - 1]) + int(s[i])))
            else:
                # Otherwise, append the character as is
                result.append(s[i])

        # Return the result as a string
        return "".join(result)


# Unit Test: s = "a1c1e1", Output: "abcdef"
assert Solution.replaceDigits("a1c1e1") == "abcdef"

# Unit Test: s = "a1b2c3d4e", Output: "abbdcfdhe"
assert Solution.replaceDigits("a1b2c3d4e") == "abbdcfdhe"

print("All unit tests are passed")
