"""914. X of a Kind in a Deck of Cards
Link: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
Difficulty: Easy
Description: You are given an integer array deck where deck[i] represents the number written on the
ith card.
Partition the cards into one or more groups such that:
Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def hasGroupsSizeX(deck: List[int]) -> bool:
        """Optimal Solution: Hash Table and Common Divisor.
           Time Complexity: O(n), Space Complexity: O(n)."""
        # Count the frequency of each card
        count = {}
        for card in deck:
            count[card] = count.get(card, 0) + 1

        # Get the list of frequencies of each card
        card_count = list(count.values())  # [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3] -> [3, 3, 6]

        # Find the smallest frequency, which represents the largest possible group size
        max_group_size = min(card_count)   # [3, 3, 6] -> 3

        # Check possible group size (from 2 to max)
        for group_size in range(2, max_group_size + 1):
            # For all card counts, check if the current group size is their common divisor
            if all(count % group_size == 0 for count in card_count):
                return True

        return False


# Input: deck = [1,2,3,4,4,3,2,1], Output: True
# Explanation: Possible partition [1,1], [2,2], [3,3], [4,4]
assert Solution.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])

# Input: deck = [1,1,1,2,2,2,3,3], Output: False
# Explanation: No possible partition
assert not Solution.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3])

# Input: deck = [1], Output: False
assert not Solution.hasGroupsSizeX([1])

# Input: desk = [1, 1, 2, 2, 2, 2], Output: True
# Explanation: Possible partition [1,1], [2,2], [2,2]
assert Solution.hasGroupsSizeX([1, 1, 2, 2, 2, 2])

# Input: desk = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3], Output: True
# Explanation: Possible partition [1,1,1], [2,2,2], [3,3,3], [3,3,3]
assert Solution.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3])

print("All unit tests are passed.")
