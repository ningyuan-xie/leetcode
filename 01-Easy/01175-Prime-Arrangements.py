"""1175. Prime Arrangements
Link: https://leetcode.com/problems/prime-arrangements/
Difficulty: Easy
Description: Return the number of permutations of 1 to n so that prime numbers are at prime indices
(1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a
product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7."""


class Solution:
    @staticmethod
    def numPrimeArrangements(n: int) -> int:
        """Optimal Solution: Sieve of Eratosthenes (used to find all prime numbers less than n).
           Time Complexity: O(n * log(log(n))), Space Complexity: O(n)"""
        # Initialize the modulo and the prime numbers from 0 to n
        MOD, prime = 10 ** 9 + 7, [True] * (n + 1)

        # Sieve of Eratosthenes
        p = 2  # Start from the first prime number
        while p * p <= n:
            if prime[p]:  # Check if p is still considered prime
                # Mark multiples of p as non-prime starting from p^2
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        # Count the number of prime numbers, excluding 0 and 1
        prime_count = sum(prime[2:])

        # Calculate the number of permutations of prime numbers using factorial
        prime_permutation = 1
        for i in range(2, prime_count + 1):
            prime_permutation = (prime_permutation * i) % MOD

        # Calculate the number of permutations of non-prime numbers using factorial
        non_prime_permutation = 1
        for i in range(2, n - prime_count + 1):
            non_prime_permutation = (non_prime_permutation * i) % MOD

        # Calculate the total number of permutations
        return (prime_permutation * non_prime_permutation) % MOD


# Unit Test: n = 5, Output: 12
# Explanation: prime numbers = [2, 3, 5], non-prime numbers = [1, 4]
# prime permutations = 3!, non-prime permutations = 2!, total permutations = 3! * 2! = 12
assert Solution.numPrimeArrangements(5) == 12

# Unit Test: n = 100, Output: 682289015
# prime permutations = 25!, non-prime permutations = 75!, total permutations = 25! * 75! = 682289015
assert Solution.numPrimeArrangements(100) == 682289015

print("All unit tests are passed.")
