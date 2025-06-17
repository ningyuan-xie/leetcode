"""965. Univalued Binary Tree
Link: https://leetcode.com/problems/univalued-binary-tree/
Difficulty: Easy
Description: A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isUnivalTree(root: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(h)"""
        # Initialize the value of the root node
        val = root.val

        def preorder_dfs(node: Optional[TreeNode]) -> bool:
            """Helper function to traverse the tree in preorder DFS"""
            # If the node is None, return True
            if not node:
                return True

            # If the node's value is not equal to the root value, return False
            if node.val != val:
                return False

            # Recursively check the left and right subtrees
            return preorder_dfs(node.left) and preorder_dfs(node.right)

        # Return the result
        return preorder_dfs(root)        


def unit_tests():
    # Input: [1,1,1,1,1,None,1], Output: True
    root = TreeNode.build_binary_tree([1, 1, 1, 1, 1, None, 1])
    assert Solution.isUnivalTree(root) is True

    # Input: [2,2,2,5,2], Output: False
    root = TreeNode.build_binary_tree([2, 2, 2, 5, 2])
    assert Solution.isUnivalTree(root) is False

    # Input: [1,1,1,1,1,None,1], Output: True
    root = TreeNode.build_binary_tree([1, 1, 1, 1, 1, None, 1])
    assert Solution.isUnivalTree(root) is True

    # Input: [9,9,9,9,9,9,9], Output: True
    root = TreeNode.build_binary_tree([9, 9, 9, 9, 9, 9, 9])
    assert Solution.isUnivalTree(root) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
