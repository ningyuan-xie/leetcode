"""1791. Find Center of Star Graph
Link: https://leetcode.com/problems/find-center-of-star-graph/
Difficulty: Easy
Description: There is an undirected star graph consisting of n nodes labeled from 1 to n. A star
graph is a graph where there is one center node and exactly n - 1 edges that connect the center node
with every other node."""

from typing import List


class Solution:
    @staticmethod
    def findCenter(edges: List[List[int]]) -> int:
        """Optimal Solution: Find Common Node. Time Complexity: O(1), Space Complexity: O(1)"""
        # The center node of the star graph will be the only node that appears in first two edges
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


# Unit Test: edges = [[1, 2], [2, 3], [4, 2]], Output: 2
assert Solution.findCenter([[1, 2], [2, 3], [4, 2]]) == 2

# Unit Test: edges = [[1, 2], [5, 1], [1, 3], [1, 4]], Output: 1
assert Solution.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1

# Unit Test: edges = [[1, 2], [2, 3]], Output: 2
assert Solution.findCenter([[1, 2], [2, 3]]) == 2

print("All unit tests are passed.")
