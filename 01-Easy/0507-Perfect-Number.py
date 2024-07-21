# Link: https://leetcode.com/problems/perfect-number/
# Difficulty: Easy
# Description: A perfect number is a positive integer that is equal to the sum of its positive divisors,
# excluding itself. A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.

class Solution:
    # Optimal Solution: Brute Force. Time Complexity: O(sqrt(n)), Space Complexity: O(1)
    @staticmethod
    def checkPerfectNumber(num: int) -> bool:
        # Return False if n is less than 2
        if num < 2:
            return False
        # Initialize a variable to store the sum of divisors: 1st divisor is 1
        divisor_sum = 1
        # Iterate through every number from 2 to the square root of n
        for i in range(2, int(num ** 0.5) + 1):  # E.g. if n = 28, check 2, 3, 4, 5
            # If i is a divisor of n
            if num % i == 0:
                # Add i to the sum of divisors
                divisor_sum += i
                # If i is not the square root of n, add n/i to the sum of divisors
                # E.g. if n = 28, num // i includes 14, 7
                if i != num // i:
                    divisor_sum += num // i

        # Return True if the sum of divisors is equal to n
        return divisor_sum == num


# Unit Test: Input = 28, Output = True.
# Explanation: 28 = 1 + 2 + 4 + 7 + 14. 1, 2, 4, 7, and 14 are divisors of 28.
assert Solution.checkPerfectNumber(28) == True

# Unit Test: Input = 6, Output = True
# Explanation: 6 = 1 + 2 + 3. 1, 2, and 3 are divisors of 6.
assert Solution.checkPerfectNumber(6) == True

# Unit Test: Input = 7, Output = False
assert Solution.checkPerfectNumber(7) == False

print("All unit tests are passed")
