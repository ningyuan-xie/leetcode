"""1128. Number of Equivalent Domino Pairs
Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
Difficulty: Easy
Description: Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if
and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated
to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is
equivalent to dominoes[j]."""

from typing import List


class Solution:
    @staticmethod
    def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize a dictionary to store the count of equivalent domino pairs
        count, num_pairs = {}, 0

        # Iterate through the list of dominoes
        for domino in dominoes:
            # Sort the domino to ensure the internal order does not matter
            domino.sort()  # [1, 2] -> [1, 2], [2, 1] -> [1, 2]

            # Convert the sorted domino to tuple to use as key in the dictionary (list is unhashable)
            domino_key = tuple(domino)  # [1, 2] -> (1, 2)

            # Increment the count of equivalent domino pairs
            num_pairs += count.get(domino_key, 0)  # 0 + 1 + 2 + 3 + 4 + 5 = 15

            # Increment the count of this domino in the dictionary
            count[domino_key] = count.get(domino_key, 0) + 1  # {(1, 2): 6}

        return num_pairs


# Unit Test: dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]], Output: 1
assert Solution.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1

# Unit Test: dominoes = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]], Output: 15
assert Solution.numEquivDominoPairs([[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]]) == 15

# Unit Test: dominoes = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]], Output: 28
assert (Solution.numEquivDominoPairs([[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [2, 1]])
        == 28)

print("All unit tests are passed.")
