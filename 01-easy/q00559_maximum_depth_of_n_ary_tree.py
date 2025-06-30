"""559. Maximum Depth of N-ary Tree
Link: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
Difficulty: Easy
Description: Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples)."""

from typing import Optional
from package.data_structures import Node


class Solution:
    @staticmethod
    def maxDepth(root: Optional[Node]) -> int:
        """Optimal Solution: Postorder DFS. Time Complexity: O(n), Space Complexity: O(n).
        Similar to 104. Maximum Depth of Binary Tree."""
        # Base Case: empty tree has depth 0
        if not root:
            return 0
        
        # Base Case: leaf node has depth 1
        if not root.children:
            return 1
        
        # Find the maximum depth among all children and add 1 for current node
        return 1 + max(Solution.maxDepth(child) for child in root.children)


def unit_tests():
    # Input: root = [1, None, 3, 2, 4, None, 5, 6], Output: 3
    root = Node.build_nary_tree([1, None, 3, 2, 4, None, 5, 6])
    assert Solution.maxDepth(root) == 3

    # Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14], Output: 5
    root = Node.build_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
    assert Solution.maxDepth(root) == 5

    # Input: root = [1, None, 2], Output: 2
    root = Node.build_nary_tree([1, None, 2])
    assert Solution.maxDepth(root) == 2

    # Input: root = [], Output: 0
    root = Node.build_nary_tree([])
    assert Solution.maxDepth(root) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
