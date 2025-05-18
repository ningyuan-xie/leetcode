"""1221. Split a String in Balanced Strings
Link: https://leetcode.com/problems/split-a-string-in-balanced-strings
Difficulty: Easy
Description: Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
- Each substring is balanced.
Return the maximum number of balanced strings you can obtain."""


class Solution:
    @staticmethod
    def balancedStringSplit(s: str) -> int:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the number of balanced strings
        count = 0

        # Initialize the number of 'L' and 'R' characters
        l_count, r_count = 0, 0

        # Increment the number of 'L' and 'R' characters
        for char in s:
            if char == 'L':
                l_count += 1
            else:
                r_count += 1
            # Greedy approach: whenever the number of 'L' and 'R' are equal,
            # increment the count and reset the number of 'L' and 'R' characters
            if l_count == r_count:
                count += 1
                l_count, r_count = 0, 0

        return count


# Unit Test: s = "RLRRLLRLRL", Output: 4
assert Solution.balancedStringSplit("RLRRLLRLRL") == 4

# Unit Test: s = "RLLLLRRRLR", Output: 3
assert Solution.balancedStringSplit("RLLLLRRRLR") == 3

# Unit Test: s = "LLLLRRRR", Output: 1
assert Solution.balancedStringSplit("LLLLRRRR") == 1

# Unit Test: s = "RLRRRLLRLL", Output: 2
assert Solution.balancedStringSplit("RLRRRLLRLL") == 2

print("All unit tests are passed.")
