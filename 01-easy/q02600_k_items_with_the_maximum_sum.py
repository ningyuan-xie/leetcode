"""2600. K Items With the Maximum Sum
Link: https://leetcode.com/problems/k-items-with-the-maximum-sum/
Difficulty: Easy
Description: There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
The bag initially contains:
- numOnes items with 1s written on them.
- numZeroes items with 0s written on them.
- numNegOnes items with -1s written on them.
We want to pick exactly k items among the available items. Return the maximum possible sum of numbers
written on the items."""


class Solution:
    @staticmethod
    def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(1), Space Complexity: O(1)."""
        # Pick all possible 1s
        ones_taken = min(k, numOnes)
        k -= ones_taken

        # Pick all possible 0s (they don't affect sum)
        zeros_taken = min(k, numZeros)
        k -= zeros_taken

        # Remaining picks must be -1s
        neg_ones_taken = min(k, numNegOnes)

        # Sum is: (+1 * ones_taken) + (0 * zeros_taken) + (-1 * neg_ones_taken)
        return ones_taken - neg_ones_taken


# Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2, Output: 2
assert Solution.kItemsWithMaximumSum(3, 2, 0, 2) == 2

# Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4, Output: 3
assert Solution.kItemsWithMaximumSum(3, 2, 0, 4) == 3

print("All unit tests are passed.")
