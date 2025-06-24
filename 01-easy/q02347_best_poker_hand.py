"""2347. Best Poker Hand
Link: https://leetcode.com/problems/best-poker-hand/
Difficulty: Easy
Description: You are given an integer array ranks and a character array suits. You have 5 cards where
the ith card has a rank of ranks[i] and a suit of suits[i].
The following are the types of poker hands you can make from best to worst:
1. "Flush": Five cards of the same suit.
2. "Three of a Kind": Three cards of the same rank.
3. "Pair": Two cards of the same rank.
4. "High Card": Any single card.
Return a string representing the best type of poker hand you can make with the given cards.
Note that the return values are case-sensitive."""

from typing import List


class Solution:
    @staticmethod
    def bestHand(ranks: List[int], suits: List[str]) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Create a hash table to store the frequency of each rank and suit
        rank_frequency, suit_frequency = {}, {}
        for i in range(5):
            rank_frequency[ranks[i]] = rank_frequency.get(ranks[i], 0) + 1
            suit_frequency[suits[i]] = suit_frequency.get(suits[i], 0) + 1
        # E.g. ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
        # -> rank_frequency = {4: 4, 2: 1}, suit_frequency = {"d": 1, "a": 2, "b": 1, "c": 1}

        # Check the type of poker hand
        if len(suit_frequency) == 1:
            return "Flush"
        if 4 in rank_frequency.values() or 3 in rank_frequency.values():
            return "Three of a Kind"
        if 2 in rank_frequency.values():
            return "Pair"
        return "High Card"


# Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"], Output: "Flush"
assert Solution.bestHand([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"]) == "Flush"

# Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"], Output: "Three of a Kind"
assert Solution.bestHand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]) == "Three of a Kind"

# Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"], Output: "Pair"
assert Solution.bestHand([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"]) == "Pair"

print("All unit tests are passed.")
