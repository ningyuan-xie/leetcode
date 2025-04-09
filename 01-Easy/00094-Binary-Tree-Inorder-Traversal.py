"""94. Binary Tree Inorder Traversal
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Difficulty: Easy
Description: Given the root of a binary tree, return the inorder traversal of its nodes' values."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        """Optimal Solution: Inorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n).
           Note: for BST, the inorder traversal will be in ascending order"""
        # Base case: if the tree root is None, return an empty list
        if not root:
            return []
        # Recursive inorder DFS traversal: left -> root -> right
        # 1. Recursive Case: Traverse the left subtree
        left_traversal = Solution.inorderTraversal(root.left)
        # 2. Root Case: Process the current node
        root_value = [root.val]
        # 3. Recursive Case: Traverse the right subtree
        right_traversal = Solution.inorderTraversal(root.right)

        # Takes effect whenever the current parent and its children have been traversed
        return left_traversal + root_value + right_traversal

    @staticmethod
    def inorderTraversalShort(root: Optional[TreeNode]) -> List[int]:
        """Optimal Solution: Inorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)"""
        # Base case: if the tree root is None, return an empty list
        if not root:
            return []
        # Recursive inorder DFS traversal: left -> root -> right
        return (Solution.inorderTraversalShort(root.left) +
                [root.val] +
                Solution.inorderTraversalShort(root.right))


# Unit Test: Input: root = [1,null,2,3], Output: [1,3,2]
root_test = TreeNode.build_binary_tree([1, None, 2, 3])
assert Solution.inorderTraversal(root_test) == [1, 3, 2]

# Unit Test: Input: root = [], Output: []
root_test = TreeNode.build_binary_tree([])
assert Solution.inorderTraversalShort(root_test) == []

# Unit Test: Input: root = [1], Output: [1]
root_test = TreeNode.build_binary_tree([1])
assert Solution.inorderTraversalShort(root_test) == [1]

print("All unit tests are passed")
