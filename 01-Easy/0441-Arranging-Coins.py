# Link: https://leetcode.com/problems/arranging-coins/
# Difficulty: Easy
# Description: You have n coins, and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    # Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)
    # Similar to 0374-Guess-Number-Higher-or-Lower.py
    @staticmethod
    def arrangeCoins(n: int) -> int:
        # Initialize the left and right pointers
        left, right = 0, n  # upper bound is n itself
        # Binary search: loop until left pointer > right pointer
        while left <= right:
            # Calculate the middle row
            mid = (left + right) // 2
            # Gauss' formula to calculate the total number of coins in the middle row
            total = mid * (mid + 1) // 2
            # The total number of coins is less than n, so the number of rows is on the right side
            if total < n:
                left = mid + 1
            # The total number of coins is greater than n, so the number of rows is on the left side
            elif total > n:
                right = mid - 1
            else:
                return mid
        # Left is the ceiling and right is the floor of the number of rows
        return right


# Unit Test: Input: n = 5, Output: 2
assert Solution.arrangeCoins(5) == 2

# Unit Test: Input: n = 8, Output: 3
assert Solution.arrangeCoins(8) == 3

# Unit Test: Input: n = 0, Output: 0
assert Solution.arrangeCoins(0) == 0

print("All unit tests are passed")
