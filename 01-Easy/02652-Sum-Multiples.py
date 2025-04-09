"""2652. Sum Multiples
Link: https://leetcode.com/problems/sum-multiples/
Difficulty: Easy
Description: Given a positive integer n, find the sum of all integers in the range [1, n] inclusive
that are divisible by 3, 5, or 7.
Return an integer denoting the sum of all numbers in the given range satisfying the constraint."""


class Solution:
    @staticmethod
    def sumOfMultiples(n: int) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize variable to track the sum of multiples
        sum_multiples = 0

        # Iterate through each number in the range [1, n]
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum_multiples += i

        return sum_multiples


# Unit Test: n = 7, Output: 21
assert Solution.sumOfMultiples(7) == 21

# Unit Test: n = 10, Output: 40
assert Solution.sumOfMultiples(10) == 40

# Unit Test: n = 9, Output: 30
assert Solution.sumOfMultiples(9) == 30

print("All unit tests are passed.")
