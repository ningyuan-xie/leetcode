"""504. Base 7
Link: https://leetcode.com/problems/base-7/
Difficulty: Easy
Description: Given an integer num, return a string of its base 7 representation."""


class Solution:
    @staticmethod
    def convertToBase7(num: int) -> str:
        """Optimal Solution: Math. Time Complexity: O(log(n)), Space Complexity: O(1).
        Similar to 405. Convert a Number to Hexadecimal."""
        # Handle the case for negative numbers
        if num < 0:
            return "-" + Solution.convertToBase7(-num)

        # Base case: if num is 0, return "0"
        if num == 0:
            return "0"

        # Initialize an empty string to store the base 7 representation
        base_7_str = ""

        # Convert the number to base 7
        while num > 0:
            base_7_str = str(num % 7) + base_7_str
            num //= 7

        return base_7_str


def unit_tests():
    # Input: num = 100, Output: "202".
    assert Solution.convertToBase7(100) == "202"

    # Input: num = -7, Output: "-10".
    assert Solution.convertToBase7(-7) == "-10"

    # Input: num = 0, Output: "0".
    assert Solution.convertToBase7(0) == "0"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
