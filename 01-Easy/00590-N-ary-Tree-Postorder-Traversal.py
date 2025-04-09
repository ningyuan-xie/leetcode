"""590. N-ary Tree Postorder Traversal
Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Difficulty: Easy
Description: Given the root of an n-ary tree, return the postorder traversal of its nodes' values."""

from typing import List
from package.data_structures import Node


class Solution:
    @staticmethod
    def postorder(root: Node) -> List[int]:
        """Optimal Solution: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)"""
        # Base Case
        if not root:
            return []
        # Initialize an empty list whenever a new parent starts
        postorder_traversal = []
        # Recursive Case: Takes effect after a sibling is traversed, so we add the current child
        # When root = leaf nodes, the loop has no effect, so the list remains []
        for child in root.children:
            postorder_traversal += Solution.postorder(child)
        # Root Case: Takes effect after all children are traversed, so we add the current parent
        postorder_traversal.append(root.val)

        return postorder_traversal


# Input: root = [1, None, 3, 2, 4, None, 5, 6], Output: [5, 6, 3, 2, 4, 1]
root_test = Node.build_nary_tree([1, None, 3, 2, 4, None, 5, 6])
assert Solution.postorder(root_test) == [5, 6, 3, 2, 4, 1]

# Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
# None, None, 11, None, 12, None, 13, None, None, 14],
# Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
root_test = Node.build_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
                                  None, None, 11, None, 12, None, 13, None, None, 14])
assert Solution.postorder(root_test) == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]

# Input: root = [1, None, 2], Output: [2, 1]
root_test = Node.build_nary_tree([1, None, 2])
assert Solution.postorder(root_test) == [2, 1]

# Input: root = [], Output: []
root_test = Node.build_nary_tree([])
assert Solution.postorder(root_test) == []

print("All unit tests are passed.")
