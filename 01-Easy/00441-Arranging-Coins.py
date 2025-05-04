"""441. Arranging Coins
Link: https://leetcode.com/problems/arranging-coins/
Difficulty: Easy
Description: You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build."""


class Solution:
    @staticmethod
    def arrangeCoins(n: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            # Calculate the total number of coins needed for mid rows
            total_coins = (mid * (mid + 1)) // 2
            if total_coins == n:
                return mid
            elif total_coins < n:
                left = mid + 1
            else:
                right = mid - 1
        # When the loop ends, left is the first row that cannot be completed and right is the last complete row
        return right


def unit_tests():
    # Input: n = 5, Output: 2
    assert Solution.arrangeCoins(5) == 2

    # Input: n = 8, Output: 3
    assert Solution.arrangeCoins(8) == 3

    # Input: n = 0, Output: 0
    assert Solution.arrangeCoins(0) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
