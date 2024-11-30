"""1945. Sum of Digits of String After Convert
Link: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
Difficulty: Easy
Description: You are given a string s consisting of lowercase English letters, and an integer k.
Your task is to convert the string into an integer by a special process, and then transform it by
summing its digits repeatedly k times. More specifically, perform the following steps:
1. Convert s into an integer by replacing each letter with its position in the alphabet (i.e.
replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
2. Transform the integer by replacing it with the sum of its digits.
3. Repeat the transform operation (step 2) k times in total.
For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following
operations:
1. Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
2. Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
3. Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above."""


class Solution:
    @staticmethod
    def getLucky(s: str, k: int) -> int:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        # Convert s to a string of digits
        digits = ""
        for char in s:
            digits += str(ord(char) - ord("a") + 1)  # E.g. "zbax" -> "262124"

        # Convert the string to an integer
        num = int(digits)

        # Perform the transformation k times
        for _ in range(k):
            num = sum(int(digit) for digit in str(num))

        return num


# Unit Test: s = "iiii", k = 1, Output: 36
assert Solution.getLucky("iiii", 1) == 36

# Unit Test: s = "leetcode", k = 2, Output: 6
assert Solution.getLucky("leetcode", 2) == 6

# Unit Test: s = "zbax", k = 2, Output: 8
assert Solution.getLucky("zbax", 2) == 8

print("All unit tests are passed")
