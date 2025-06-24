"""1046. Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/
Difficulty: Easy
Description: You are given an array of integers stones where stones[i] is the weight of the ith
stone. We are playing a game with the stones. On each turn, we choose the heaviest two stones
and smash them together. Suppose the heaviest two stones have weights x and y with x <= y.
The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0."""

from typing import List
import heapq  # Priority Queue (Heap) Module


class Solution:
    @staticmethod
    def lastStoneWeight(stones: List[int]) -> int:
        """Optimal Solution: Min Heap. Time Complexity: O(n * log(n)), Space Complexity: O(n).
           Similar to 0703-Kth-Largest-Element-in-a-Stream.py"""
        # Python's heapq is a min heap, but we need a max heap to pick the heaviest stones
        stones = [-stone for stone in stones]  # [2, 7, 4, 1, 8, 1] -> [-2, -7, -4, -1, -8, -1]
        heapq.heapify(stones)  # [-8, -7, -4, -1, -2, -1]

        # While there are more than one stone left
        while len(stones) > 1:
            # Get the two heaviest stones
            y = -heapq.heappop(stones)  # This is 8 (original value)
            x = -heapq.heappop(stones)  # This is 7 (original value)

            # If the two stones are not equal, add the difference back to the heap
            if x != y:
                heapq.heappush(stones, -abs(x - y))  # 8 - 7 = 1, so we push -1

        # Return the last stone weight if there is one stone left, otherwise return 0
        return -stones[0] if stones else 0


# Input: stones = [2, 7, 4, 1, 8, 1], Output: 1
assert Solution.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1

# Input: stones = [1, 3], Output: 2
assert Solution.lastStoneWeight([1, 3]) == 2

# Input: stones = [2, 2], Output: 0
assert Solution.lastStoneWeight([2, 2]) == 0

print("All unit tests are passed.")
