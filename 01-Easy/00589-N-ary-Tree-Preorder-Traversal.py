"""589. N-ary Tree Preorder Traversal
Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Difficulty: Easy
Description: Given the root of an n-ary tree, return the preorder traversal of its nodes' values."""

from typing import List
from package.data_structures import Node


class Solution:
    @staticmethod
    def preorder(root: Node) -> List[int]:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case
        if not root:
            return []
        # Root Case: Initialize an empty list and add the current parent whenever a new parent starts
        preorder_traversal = [root.val]
        # Recursive Case: Takes effect whenever a new sibling starts
        # When root = leaf nodes, the loop has no effect, so the list remains [root.val] and returns
        for child in root.children:
            preorder_traversal += Solution.preorder(child)

        return preorder_traversal


# Input: root = [1, None, 3, 2, 4, None, 5, 6], Output: [1, 3, 5, 6, 2, 4]
root_test = Node.build_nary_tree([1, None, 3, 2, 4, None, 5, 6])
assert Solution.preorder(root_test) == [1, 3, 5, 6, 2, 4]

# Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
# None, None, 11, None, 12, None, 13, None, None, 14],
# Output: [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
root_test = Node.build_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
                                  None, None, 11, None, 12, None, 13, None, None, 14])
assert Solution.preorder(root_test) == [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

# Input: root = [1, None, 2], Output: [1, 2]
root_test = Node.build_nary_tree([1, None, 2])
assert Solution.preorder(root_test) == [1, 2]

# Input: root = [], Output: []
root_test = Node.build_nary_tree([])
assert Solution.preorder(root_test) == []

print("All unit tests are passed.")
