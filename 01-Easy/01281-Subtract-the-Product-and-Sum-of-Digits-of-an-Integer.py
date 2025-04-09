"""1281. Subtract the Product and Sum of Digits of an Integer
Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Difficulty: Easy
Description: Given an integer number n, return the difference between the product of its digits
and the sum of its digits."""


class Solution:
    @staticmethod
    def subtractProductAndSum(n: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Initialize the product and sum of the digits
        product_of_digits, sum_of_digits = 1, 0

        # Calculate the product and sum of the digits
        while n > 0:
            digit = n % 10
            product_of_digits *= digit
            sum_of_digits += digit
            n //= 10

        return product_of_digits - sum_of_digits


# Unit Test: n = 234, Output: 15
assert Solution.subtractProductAndSum(234) == 15

# Unit Test: n = 4421, Output: 21
assert Solution.subtractProductAndSum(4421) == 21

print("All unit tests are passed.")
