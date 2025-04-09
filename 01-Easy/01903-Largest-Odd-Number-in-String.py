"""1903. Largest Odd Number in String
Link: https://leetcode.com/problems/largest-odd-number-in-string/
Difficulty: Easy
Description: You are given a string num, representing a large integer. Return the largest-valued
odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd
integer exists.
A substring is a contiguous sequence of characters within a string."""


class Solution:
    @staticmethod
    def largestOddNumber(num: str) -> str:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Find the largest odd number
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""


# Unit Test: num = "52", Output: "5"
assert Solution.largestOddNumber("52") == "5"

# Unit Test: num = "4206", Output: ""
assert Solution.largestOddNumber("4206") == ""

# Unit Test: num = "35427", Output: "35427"
assert Solution.largestOddNumber("35427") == "35427"

print("All unit tests are passed.")
