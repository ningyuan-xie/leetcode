"""3560. Find Minimum Log Transportation Cost
Link: https://leetcode.com/problems/find-minimum-log-transportation-cost/
Difficulty: Easy
Description: You are given integers n, m, and k.
There are two logs of lengths n and m units, which need to be transported in three trucks where each truck can carry one log with length at most k units.
You may cut the logs into smaller pieces, where the cost of cutting a log of length x into logs of length len1 and len2 is cost = len1 * len2 such that len1 + len2 = x.
Return the minimum total cost to distribute the logs onto the trucks. If the logs don't need to be cut, the total cost is 0."""


class Solution:
    @staticmethod
    def minCuttingCost(n: int, m: int, k: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # If no cutting needed (both logs fit in trucks)
        if n <= k and m <= k:
            return 0
        
        # Calculate minimum cuts needed and cost
        cuts_needed = max(n, m) - k
        return cuts_needed * (max(n, m) - cuts_needed)
    

def unit_tests():
    # Input: n = 6, m = 5, k = 5, Output: 5
    assert Solution.minCuttingCost(6, 5, 5) == 5

    # Input: n = 4, m = 4, k = 6, Output: 0
    assert Solution.minCuttingCost(4, 4, 6) == 0

    # Input: n = 1, m = 4, k = 2, Output: 4
    assert Solution.minCuttingCost(1, 4, 2) == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
    