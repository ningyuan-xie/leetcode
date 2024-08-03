"""504. Base 7
Link: https://leetcode.com/problems/base-7/
Difficulty: Easy
Description: Given an integer num, return a string of its base 7 representation."""


class Solution:
    @staticmethod
    def convertToBase7(num: int) -> str:
        """Optimal Solution: Iterative Division. Time Complexity: O(log(n)), Space Complexity: O(log(n)).
           Similar to 0405-Convert-a-Number-to-Hexadecimal.py"""
        # Base Case: If the number is 0, return "0"
        if num == 0:
            return "0"
        # Initialize the result string and the sign
        result = ""
        sign, num = ("-", -num) if num < 0 else ("", num)
        # Iterate through the iterative division process from RIGHT to LEFT
        while num > 0:
            remainder = num % 7
            # Append the remainder to the front of the result string
            result = str(remainder) + result
            # Divide the number by 7 using floor division to move to the next digit on the left
            num //= 7
        # Return the base 7 representation of the number
        return sign + result


# Unit Test: Input: num = 100, Output: "202". Explanation: 100 = 2*7^2 + 0*7^1 + 2*7^0 = 202
assert Solution.convertToBase7(100) == "202"

# Unit Test: Input: num = -7, Output: "-10". Explanation: -7 = -1*7^1 + 0*7^0 = -10
assert Solution.convertToBase7(-7) == "-10"

# Unit Test: Input: num = 0, Output: "0". Explanation: 0 = 0*7^0 = 0
assert Solution.convertToBase7(0) == "0"

print("All unit tests are passed")
