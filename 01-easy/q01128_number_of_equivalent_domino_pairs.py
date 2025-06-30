"""1128. Number of Equivalent Domino Pairs
Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
Difficulty: Easy
Description: Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j]."""

from typing import List


class Solution:
    @staticmethod
    def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize a dictionary to store the count of equivalent domino pairs
        count, num_pairs = {}, 0

        # Iterate through the list of dominoes
        for domino in dominoes:
            # Create a normalized key by taking min and max to avoid sorting
            domino_key = (min(domino[0], domino[1]), max(domino[0], domino[1]))

            # Increment the count of equivalent domino pairs
            num_pairs += count.get(domino_key, 0)

            # Increment the count of this domino in the dictionary
            count[domino_key] = count.get(domino_key, 0) + 1

        return num_pairs


def unit_tests():
    # Input: dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]], Output: 1
    assert Solution.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1

    # Input: dominoes = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]], Output: 15
    assert Solution.numEquivDominoPairs([[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]]) == 15

    # Input: dominoes = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]], Output: 28
    assert Solution.numEquivDominoPairs([[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]]) == 28


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
