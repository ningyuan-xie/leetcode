"""762. Prime Number of Set Bits in Binary Representation
Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
Difficulty: Easy
Description: Given two integers left and right, return the count of numbers in the inclusive
range [left, right] having a prime number of set bits in their binary representation.
Recall that the number of set bits an integer has is the number of 1's present when written
in binary."""


class Solution:
    @staticmethod
    def count_prime_set_bits(left: int, right: int) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the count of numbers having a prime number of set bits
        count = 0

        # Define the set of prime numbers less than 32, which is the max number of bits in an integer
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        # Check each number in the range [left, right]
        for num in range(left, right + 1):
            # Count the number of set bits in the binary representation of the number
            set_bits = bin(num).count('1')

            # Check if the number of set bits is a prime number
            if set_bits in primes:
                count += 1

        return count


# Unit Test: Input: left = 6, right = 10, Output: 4
assert Solution.count_prime_set_bits(6, 10) == 4

# Unit Test: Input: left = 10, right = 15, Output: 5
assert Solution.count_prime_set_bits(10, 15) == 5

# Unit Test: Input: left = 10, right = 20, Output: 9
assert Solution.count_prime_set_bits(10, 20) == 9

print("All unit tests are passed")
