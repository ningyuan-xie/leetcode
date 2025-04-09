"""2864. Maximum Odd Binary Number
Link: https://leetcode.com/problems/maximum-odd-binary-number/
Difficulty: Easy
Description: You are given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number is the maximum
odd binary number that can be created from this combination.
Return a string representing the maximum odd binary number that can be created from the given
combination.
Note that the resulting string can have leading zeros."""


class Solution:
    @staticmethod
    def maximumOddBinaryNumber(s: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        # Find the number of 1's in the string
        count_1 = s.count('1')

        # Return the maximum odd binary number
        return '1' * (count_1 - 1) + '0' * (len(s) - count_1) + '1'


# Unit Test: s = "010", Output: "001"
assert Solution.maximumOddBinaryNumber("010") == "001"

# Unit Test: s = "0101", Output: "1001"
assert Solution.maximumOddBinaryNumber("0101") == "1001"

print("All unit tests are passed")
