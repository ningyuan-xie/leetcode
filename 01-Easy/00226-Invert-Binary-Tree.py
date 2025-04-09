"""226. Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Difficulty: Easy
Description: Invert a binary tree."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Preorder because need to process the current node before the left and right subtrees"""
        # Base case: if the tree root is None, return None
        if not root:
            return None
        # 1. Root Case: Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        # 2. Recursive Case: Invert the left and right subtrees
        Solution.invertTree(root.left)
        # 3. Recursive Case: Invert the right subtree
        Solution.invertTree(root.right)
        return root


# Input: [4, 2, 7, 1, 3, 6, 9], Output: [4, 7, 2, 9, 6, 3, 1]
root_test = TreeNode.build_binary_tree([4, 2, 7, 1, 3, 6, 9])
root_expected = TreeNode.build_binary_tree([4, 7, 2, 9, 6, 3, 1])
assert Solution.invertTree(root_test) == root_expected

# Input: [2, 1, 3], Output: [2, 3, 1]
root_test = TreeNode.build_binary_tree([2, 1, 3])
root_expected = TreeNode.build_binary_tree([2, 3, 1])
assert Solution.invertTree(root_test) == root_expected

print("All unit tests are passed.")
