"""1544. Make The String Great
Link: https://leetcode.com/problems/make-the-string-great/
Difficulty: Easy
Description: Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
- 0 <= i <= s.length - 2
- s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and
remove them. You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given
constraints.
Notice that an empty string is also good."""


class Solution:
    @staticmethod
    def makeGood(s: str) -> str:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the stack to store the characters
        stack = []

        # Iterate through the string
        for char in s:
            # Check if the stack is not empty and the top of the stack is the same letter but
            # different case, such as 'E' and 'e'
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()  # Pop the top of the stack
            else:
                stack.append(char)  # Push the character onto the stack

        # Join the characters in the stack into a single string
        return ''.join(stack)


# Unit Test: s = "leEeetcode", Output: "leetcode"
assert Solution.makeGood("leEeetcode") == "leetcode"

# Unit Test: s = "abBAcC", Output: ""
assert Solution.makeGood("abBAcC") == ""

# Unit Test: s = "s", Output: "s"
assert Solution.makeGood("s") == "s"

print("All unit tests are passed")
