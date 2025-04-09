"""1560. Most Visited Sector in a Circular Track
Link: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
Difficulty: Easy
Description: Given an integer n and an integer array rounds. We have a circular track which consists
of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of
m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example,
round 1 starts at sector rounds[0] and ends at sector rounds[1]
Return an array of the most visited sectors sorted in ascending order.
Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise
direction."""

from typing import List


class Solution:
    @staticmethod
    def mostVisited(n: int, rounds: List[int]) -> List[int]:
        """Optimal Solution: Circular Traversal. Time Complexity: O(m), Space Complexity: O(1)"""
        # Initialize the start and end sectors of the marathon
        start_sector = rounds[0]
        end_sector = rounds[-1]

        # If start sector <= end sector, the most visited sectors are from start to end
        if start_sector <= end_sector:
            # E.g. rounds = [2, 1, 3] -> start_sector = 2, end_sector = 3 -> return [2, 3]
            return list(range(start_sector, end_sector + 1))

        # If start sector > end sector, the most visited sectors are from 1 to end and from start to n
        else:
            # E.g. rounds = [3, 2, 1] -> start_sector = 3, end_sector = 1 -> return [1, 2, 3]
            return (list(range(1, end_sector + 1))
                    + list(range(start_sector, n + 1)))


# Unit Test: n = 4, rounds = [1, 3, 1, 2], Output: [1, 2]
assert Solution.mostVisited(4, [1, 3, 1, 2]) == [1, 2]

# Unit Test: n = 2, rounds = [2, 1, 2, 1, 2, 1, 2, 1, 2], Output: [2]
assert Solution.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2]

# Unit Test: n = 7, rounds = [1, 3, 5, 7], Output: [1, 2, 3, 4, 5, 6, 7]
assert Solution.mostVisited(7, [1, 3, 5, 7]) == [1, 2, 3, 4, 5, 6, 7]

print("All unit tests are passed.")
