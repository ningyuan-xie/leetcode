# Link: https://leetcode.com/problems/add-digits/
# Difficulty: Easy
# Description: Given an integer num, repeatedly add its digits
# until the result has only one digit, and return it.


class Solution:
    # Optimal Solution: Digital Root. Time Complexity: O(1), Space Complexity: O(1)
    @staticmethod
    def addDigits(n: int) -> int:
        # The digital root (dr) of a number is given by the formula:
        # dr(n) = 1 + ((n - 1) % 9)
        return 1 + ((n - 1) % 9) if n > 0 else 0
        # E.g. dr(38) = 1 + ((38 - 1) % 9) = 1 + (37 % 9) = 1 + 1 = 2
        # E.g. dr(0) = 1 + ((0 - 1) % 9) = 1 + (-1 % 9) = 1 + -1 = 0

    # Alternative Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n))
    @staticmethod
    def addDigits_2(n: int) -> int:
        # Base case: if the number is less than 10, return the number
        if n < 10:
            return n

        # Initialize a variable to store the sum of the digits
        sum_digits = 0

        # Iterate through the digits of the number
        while n > 0:
            # Add the last digit to the sum
            sum_digits += n % 10
            # Remove the last digit from the number
            n //= 10

        # Recursively call the function with the sum of the digits
        return Solution.addDigits_2(sum_digits)


# Unit Test: Input: num = 38, Output: 2
assert Solution.addDigits(38) == 2

# Unit Test: Input: num = 0, Output: 0
assert Solution.addDigits_2(0) == 0

# Unit Test: Input: num = 9, Output: 9
assert Solution.addDigits_2(9) == 9

print("All unit tests are passed")
