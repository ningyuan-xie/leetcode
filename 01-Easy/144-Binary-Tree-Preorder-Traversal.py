"""144. Binary Tree Preorder Traversal
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Difficulty: Easy
Description: Given the root of a binary tree, return the preorder traversal of its nodes' values."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 0094-Binary-Tree-Inorder-Traversal.py"""
        # Base case: if the tree root is None, return an empty list
        if not root:
            return []
        # Recursive preorder DFS traversal: root -> left -> right
        # 1. Root Case: Process the current node
        root_value = [root.val]
        # 2. Recursive Case: Traverse the left subtree
        left_traversal = Solution.preorderTraversal(root.left)
        # 3. Recursive Case: Traverse the right subtree
        right_traversal = Solution.preorderTraversal(root.right)

        # Takes effect whenever the current parent and its children have been traversed
        return root_value + left_traversal + right_traversal


# Unit Test: Input: root = [1,null,2,3], Output: [1,2,3]
root_test = TreeNode.build_binary_tree([1, None, 2, 3])
assert Solution.preorderTraversal(root_test) == [1, 2, 3]

# Unit Test: Input: root = [], Output: []
root_test = TreeNode.build_binary_tree([])
assert Solution.preorderTraversal(root_test) == []

# Unit Test: Input: root = [1], Output: [1]
root_test = TreeNode.build_binary_tree([1])
assert Solution.preorderTraversal(root_test) == [1]

print("All unit tests are passed")
