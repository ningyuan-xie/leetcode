"""3502. Minimum Cost to Reach Every Position
Link: https://leetcode.com/problems/minimum-cost-to-reach-every-position/
Difficulty: Easy
Description: You are given an integer array cost of size n. You are currently at position n (at the end of the line) in a line of n + 1 people (numbered from 0 to n).
You wish to move forward in the line, but each person in front of you charges a specific amount to swap places. The cost to swap with person i is given by cost[i].
You are allowed to swap places with people as follows:
• If they are in front of you, you must pay them cost[i] to swap with them.
• If they are behind you, they can swap with you for free.
Return an array answer of size n, where answer[i] is the minimum total cost to reach each position i in the line."""

from typing import List


class Solution:
    @staticmethod
    def minCosts(cost: List[int]) -> List[int]:
        """Optimal Solution: Min Prefix Array. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(cost)
        # Initialize the result array with the first element of cost
        result = [cost[0]] * n
        # Initialize the minimum prefix sum with the first element of cost
        min_prefix_sum = cost[0]

        # Iterate through the cost array starting from the second element
        for i in range(1, n):
            # Update the minimum prefix sum
            min_prefix_sum = min(min_prefix_sum, cost[i])
            # Calculate the minimum cost to reach position i
            result[i] = min_prefix_sum

        return result


def unit_tests():
    # Input: cost = [5,3,4,1,3,2], Output: [5,3,3,1,1,1]
    assert Solution.minCosts([5, 3, 4, 1, 3, 2]) == [5, 3, 3, 1, 1, 1]

    # Input: cost = [1,2,4,6,7], Output: [1,1,1,1,1]
    assert Solution.minCosts([1, 2, 4, 6, 7]) == [1, 1, 1, 1, 1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
