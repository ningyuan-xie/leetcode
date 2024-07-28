# Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Difficulty: Easy
# Description: Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

from typing import List
from package.data_structures import Node


class Solution:
    # Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def preorder(root: Node) -> List[int]:
        # Base Case
        if not root:
            return []
        # Root Case: Initialize an empty list and add the current parent whenever a new parent starts
        preorder_traversal = [root.val]
        # Recursive Case: Add the current child
        for child in root.children:
            preorder_traversal += Solution.preorder(child)

        return preorder_traversal


# Unit Test: Input: root = [1, None, 3, 2, 4, None, 5, 6], Output: [1, 3, 5, 6, 2, 4]
root_test = Node.build_nary_tree([1, None, 3, 2, 4, None, 5, 6])
assert Solution.preorder(root_test) == [1, 3, 5, 6, 2, 4]

# Unit Test: Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
# None, None, 11, None, 12, None, 13, None, None, 14],
# Output: [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
root_test = Node.build_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
                                  None, None, 11, None, 12, None, 13, None, None, 14])
assert Solution.preorder(root_test) == [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

# Unit Test: Input: root = [1, None, 2], Output: [1, 2]
root_test = Node.build_nary_tree([1, None, 2])
assert Solution.preorder(root_test) == [1, 2]

# Unit Test: Input: root = [], Output: []
root_test = Node.build_nary_tree([])
assert Solution.preorder(root_test) == []

print("All unit tests are passed")
