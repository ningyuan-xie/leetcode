"""145. Binary Tree Postorder Traversal
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Difficulty: Easy
Description: Given the root of a binary tree, return the postorder traversal of its nodes' values."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
        """Optimal Solution: Postorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case: If the root is None, return an empty list
        if not root:
            return []

        # Recursive Case: left -> right -> root
        return Solution.postorderTraversal(root.left) + Solution.postorderTraversal(root.right) + [root.val]


def unit_tests():
    # Input: root = [1,null,2,3], Output: [3,2,1]
    root = TreeNode.build_binary_tree([1, None, 2, 3])
    assert Solution.postorderTraversal(root) == [3, 2, 1]

    # Input: root = [], Output: []
    root = TreeNode.build_binary_tree([])
    assert Solution.postorderTraversal(root) == []

    # Input: root = [1], Output: [1]
    root = TreeNode.build_binary_tree([1])
    assert Solution.postorderTraversal(root) == [1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
