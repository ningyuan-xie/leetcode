"""2810. Faulty Keyboard
Link: https://leetcode.com/problems/faulty-keyboard/
Difficulty: Easy
Description: Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it
reverses the string that you have written. Typing other characters works as expected.
You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.
Return the final string that will be present on your laptop screen."""


class Solution:
    @staticmethod
    def finalString(s: str) -> str:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)"""
        stack = []
        for char in s:
            if char == 'i':
                stack.reverse()
            else:
                stack.append(char)
        return ''.join(stack)


# Unit Test: s = "string", Output: "rtsng"
assert Solution.finalString("string") == "rtsng"

# Unit Test: s = "poiinter", Output: "ponter"
assert Solution.finalString("poiinter") == "ponter"

print("All unit tests are passed")
