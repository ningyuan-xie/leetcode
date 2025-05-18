"""226. Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Difficulty: Easy
Description: Given the root of a binary tree, invert the tree, and return its root."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case: If the tree is empty, return None
        if not root:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        Solution.invertTree(root.left)
        Solution.invertTree(root.right)

        return root


def unit_tests():
    # Input: [4, 2, 7, 1, 3, 6, 9], Output: [4, 7, 2, 9, 6, 3, 1]
    root = TreeNode.build_binary_tree([4, 2, 7, 1, 3, 6, 9])
    output = TreeNode.build_binary_tree([4, 7, 2, 9, 6, 3, 1])
    assert Solution.invertTree(root) == output

    # Input: [2, 1, 3], Output: [2, 3, 1]
    root = TreeNode.build_binary_tree([2, 1, 3])
    output = TreeNode.build_binary_tree([2, 3, 1])
    assert Solution.invertTree(root) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
