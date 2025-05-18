"""507. Perfect Number
Link: https://leetcode.com/problems/perfect-number/
Difficulty: Easy
Description: A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false."""


class Solution:
    @staticmethod
    def checkPerfectNumber(num: int) -> bool:
        """Optimal Solution: Math. Time Complexity: O(sqrt(n)), Space Complexity: O(1)."""
        # Handle edge cases
        if num <= 1:
            return False
        
        # Initialize sum with 1
        divisor_sum = 1

        # Iterate through every number from 2 to the square root of n
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                # Add both divisor and its complement
                divisor_sum += i
                complement = num // i
                if complement != i:
                    divisor_sum += complement

        # Return True if the sum of divisors is equal to n
        return divisor_sum == num


def unit_tests():
    # Input = 28, Output = True
    assert Solution.checkPerfectNumber(28) is True

    # Input = 6, Output = True
    assert Solution.checkPerfectNumber(6) is True

    # Input = 7, Output = False
    assert Solution.checkPerfectNumber(7) is False


if __name__ == "__main__":
    unit_tests()    
    print("All unit tests are passed.")
