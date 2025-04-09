"""3345. Smallest Divisible Digit Product I
Link: https://leetcode.com/problems/smallest-divisible-digit-product-i/
Difficulty: Easy
Description: You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t."""


class Solution:
    @staticmethod
    def smallestNumber(n: int, t: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        # If n is 0 and t is not 0, return t
        if n == 0:
            return t

        def product_of_digits(num: int) -> int:
            """Helper function to calculate the product of digits."""
            product = 1
            for digit in str(num):
                product *= int(digit)
            return product
        
        # Iterate from n to 10^9
        for i in range(n, 10**9 + 1):
            # Check if the product of digits is divisible by t
            if product_of_digits(i) % t == 0:
                return i


def unit_tests():
    # Input: n = 10, t = 2, Output: 10
    assert Solution.smallestNumber(10, 2) == 10

    # Input: n = 15, t = 3, Output: 16
    assert Solution.smallestNumber(15, 3) == 16


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed")
