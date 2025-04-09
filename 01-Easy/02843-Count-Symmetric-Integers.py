"""2843. Count Symmetric Integers
Link: https://leetcode.com/problems/count-symmetric-integers/
Difficulty: Easy
Description: You are given two positive integers low and high.
An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal
to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
Return the number of symmetric integers in the range [low, high]."""


class Solution:
    @staticmethod
    def countSymmetricIntegers(low: int, high: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the count of symmetric integers
        count = 0

        def isSymmetric(num: int) -> bool:
            """Helper function to check if a number is symmetric"""
            num_str = str(num)
            if len(num_str) % 2 != 0:
                return False

            n = len(num_str) // 2
            return sum(int(digit) for digit in num_str[:n]) == sum(int(digit) for digit in num_str[n:])

        # Count the number of symmetric integers
        for number in range(low, high + 1):
            if isSymmetric(number):
                count += 1
        return count


# Unit Test: low = 1, high = 100, Output: 9
assert Solution.countSymmetricIntegers(1, 100) == 9

# Unit Test: low = 1200, high = 1230, Output: 4
assert Solution.countSymmetricIntegers(1200, 1230) == 4

print("All unit tests are passed.")
