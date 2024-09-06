"""965. Univalued Binary Tree
Link: https://leetcode.com/problems/univalued-binary-tree/
Difficulty: Easy
Description: A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isUnivalTree(root: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(h)"""
        # Initialize the value of the root node
        val = root.val

        def preorder_dfs_not_equal(node: Optional[TreeNode]) -> bool:
            """Helper function to traverse the tree in preorder DFS"""
            # If the node is None, return True (empty subtree is considered univalued)
            if not node:
                return True

            # If the node's value is not equal to the root value, return False
            if node.val != val:
                return False

            # Recursively check the left and right subtrees
            return preorder_dfs_not_equal(node.left) and preorder_dfs_not_equal(node.right)

        def preorder_dfs_equal(node: Optional[TreeNode]) -> bool:
            """Helper function (alternative) to traverse the tree in preorder DFS"""
            # If the node is None, return True (empty subtree is considered univalued)
            if not node:
                return True

            # Check if the current node matches the value
            if node.val == val:
                # Recursively check the left and right subtrees
                return preorder_dfs_equal(node.left) and preorder_dfs_equal(node.right)

            # If the current node's value doesn't match, return False
            return False

        # Return the result
        return preorder_dfs_equal(root)


# Unit Test: Input: [1,1,1,1,1,None,1], Output: True
root_test = TreeNode.build_binary_tree([1, 1, 1, 1, 1, None, 1])
assert Solution.isUnivalTree(root_test) is True

# Unit Test: Input: [2,2,2,5,2], Output: False
root_test = TreeNode.build_binary_tree([2, 2, 2, 5, 2])
assert Solution.isUnivalTree(root_test) is False

# Unit Test: Input: [1,1,1,1,1,None,1], Output: True
root_test = TreeNode.build_binary_tree([1, 1, 1, 1, 1, None, 1])
assert Solution.isUnivalTree(root_test) is True

# Unit Test: Input: [9,9,9,9,9,9,9], Output: True
root_test = TreeNode.build_binary_tree([9, 9, 9, 9, 9, 9, 9])
assert Solution.isUnivalTree(root_test) is True

print("All unit tests are passed")
