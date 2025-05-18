"""2558. Take Gifts From the Richest Pile
Link: https://leetcode.com/problems/take-gifts-from-the-richest-pile
Difficulty: Easy
Description: You are given an integer array gifts denoting the number of gifts in various piles.
Every second, you do the following:
- Choose the pile with the maximum number of gifts.
- If there is more than one pile with the maximum number of gifts, choose any.
- Reduce the number of gifts in the pile to the floor of the square root of the original number of
gifts in the pile.
Return the number of gifts remaining after k seconds."""

from typing import List
import heapq


class Solution:
    @staticmethod
    def pickGifts(gifts: List[int], k: int) -> int:
        """Optimal Solution: Min Heap. Time Complexity: O(k * log(n)), Space Complexity: O(n).
           Use a min heap to store the "largest" number of gifts in the pile"""
        # Python's heapq is a min heap, so we need a max heap to store the negative number of gifts
        max_heap = [-gift for gift in gifts]  # [25, 64, 9, 4, 100] -> [-25, -64, -9, -4, -100]
        heapq.heapify(max_heap)   # [-100, -64, -9, -4, -25]

        # Perform k seconds of gift-taking
        for _ in range(k):
            # Take the maximum number of gifts using heappop (extractMin)
            max_gifts = -heapq.heappop(max_heap)  # 100 -> 64 -> 25 -> 10

            # Update the number of gifts in the pile using heappush (insert)
            heapq.heappush(max_heap, -int(max_gifts ** 0.5))

        # Return the total number of gifts remaining: [-9, -8, -5, -4, -3]
        return sum(-gift for gift in max_heap)


# Unit Test: gifts = [25,64,9,4,100], k = 4, Output: 29
assert Solution.pickGifts([25, 64, 9, 4, 100], 4) == 29

# Unit Test: gifts = [1,1,1,1], k = 4, Output: 4
assert Solution.pickGifts([1, 1, 1, 1], 4) == 4

print("All unit tests are passed.")
