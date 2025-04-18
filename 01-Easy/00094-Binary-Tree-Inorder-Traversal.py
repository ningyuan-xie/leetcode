"""94. Binary Tree Inorder Traversal
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Difficulty: Easy
Description: Given the root of a binary tree, return the inorder traversal of its nodes' values."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        """Optimal Solution: Inorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case: If the root is None, return an empty list
        if not root:
            return []
        # Recursive Case: left -> root -> right
        return Solution.inorderTraversal(root.left) + [root.val] + Solution.inorderTraversal(root.right)


def unit_tests():
    # Input: root = [1,null,2,3], Output: [1,3,2]
    root = TreeNode.build_binary_tree([1, None, 2, 3])
    assert Solution.inorderTraversal(root) == [1, 3, 2]

    # Input: root = [], Output: []
    root = TreeNode.build_binary_tree([])
    assert Solution.inorderTraversal(root) == []

    # Input: root = [1], Output: [1]
    root = TreeNode.build_binary_tree([1])
    assert Solution.inorderTraversal(root) == [1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
