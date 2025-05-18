"""1971. Find if Path Exists in Graph
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
Difficulty: Easy
Description: There is a bi-directional graph with n vertices, where each vertex is labeled from
0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where
each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every
vertex pair is connected by at most one edge, and no vertex has an edge to itself.
You want to determine if there is a valid path that exists from vertex source to vertex destination.
Given edges and the integers n, source, and destination, return true if there is a valid path from
source to destination, or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 0463-Island-Perimeter.py"""
        # Initialize the graph as a dictionary
        graph = {i: [] for i in range(n)}  # E.g. n = 3 -> {0: [], 1: [], 2: []}

        # Build the graph: E.g. edges = [[0, 1], [1, 2], [2, 0]]
        for (u, v) in edges:  # graph = {0: [1, 2], 1: [0, 2], 2: [1, 0]}
            graph[u].append(v)
            graph[v].append(u)

        # Initialize the visited set
        visited = set()

        def preorder_dfs(node: int) -> bool:
            """Helper function to perform preorder DFS traversal"""
            # Base case: If we have reached the destination node, return True
            if node == destination:
                return True
            # Base case: If the node has already been visited, return False to avoid cycles
            if node in visited:
                return False

            # 1. Root case: Mark the current node as visited
            visited.add(node)

            # Iterate through each neighbor connected to the current node
            for neighbor in graph[node]:  # E.g. graph[0] = [1, 2] -> neighbor = 1, 2
                # 2. Recursive case: Perform DFS on the neighbor
                if preorder_dfs(neighbor):  # If any neighbor leads to the destination, return True
                    return True

            # If no path to the destination was found through this node, return False
            return False

        return preorder_dfs(source)


# Unit Test: n = 3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, destination = 2, Output: True
assert Solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True

# Unit Test: n = 6, edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source = 0, destination = 5,
# Output: False
# assert (Solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
#         is False)

# Unit Test: n = 1, edges = [], source = 0, destination = 0, Output: True
# assert Solution.validPath(1, [], 0, 0) is True

print("All unit tests are passed.")
