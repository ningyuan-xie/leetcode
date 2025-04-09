"""2696. Minimum String Length After Removing Substrings
Link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
Difficulty: Easy
Description: You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, you can remove any occurrence
of one of the substrings "AB" or "CD" from s.
Return the minimum possible length of the resulting string that you can obtain.
Note that the string concatenates after removing the substring and could produce new "AB" or "CD"
substrings."""


class Solution:
    @staticmethod
    def minLength(s: str) -> int:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the stack to track the characters
        stack = []

        # Iterate through the string
        for char in s:
            # If the stack is not empty and the current character is 'B' and the top of the stack is 'A'
            if stack and char == 'B' and stack[-1] == 'A':
                stack.pop()
            # If the stack is not empty and the current character is 'D' and the top of the stack is 'C'
            elif stack and char == 'D' and stack[-1] == 'C':
                stack.pop()
            # Otherwise, append the current character to the stack
            else:
                stack.append(char)

        # Return the length of the stack
        return len(stack)


# Unit Test: s = "ABFCACDB", Output: 2
assert Solution.minLength("ABFCACDB") == 2

# Unit Test: s = "ACBBD", Output: 5
assert Solution.minLength("ACBBD") == 5

print("All unit tests are passed.")
