# Link: https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy
# Description: Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1)
    # The trick is while calculating the height, use height to also get the diameter
    # Similar to 0104-Maximum-Depth-of-Binary-Tree.py
    @staticmethod
    def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
        # Initialize the diameter of the binary tree
        diameter = 0

        # Helper function: Postorder DFS Traversal: left -> right -> root
        # Postorder because we need to calculate the height of the left and right subtrees first
        def postorder_dfs_traversal(node: TreeNode) -> int:
            # nonlocal variables to access the outer scope mutable variables
            nonlocal diameter
            # Base Case: If the current node is None, return -1
            if not node:
                return -1
            # Recursive postorder DFS traversal: left -> right -> root
            # 1. Recursive Case: Traverse the left subtree
            left_height = postorder_dfs_traversal(node.left)
            # 2. Recursive Case: Traverse the right subtree
            right_height = postorder_dfs_traversal(node.right)
            # 3. Root Case: Process the current node and update the diameter of the binary tree
            # The + 2 accounts for the two edges that connect the node to its left and right subtrees,
            # as these edges are not included in the heights of the subtrees themselves
            diameter = max(diameter, left_height + right_height + 2)

            # Return the height of the current node
            return max(left_height, right_height) + 1

        # Perform postorder traversal
        postorder_dfs_traversal(root)
        return diameter


# Unit Test: Input: root = [1, 2, 3, 4, 5], Output: 3
root_test = TreeNode.build_binary_tree([1, 2, 3, 4, 5])
assert Solution.diameterOfBinaryTree(root_test) == 3

# Unit Test: Input: root = [1, 2], Output: 1
root_test = TreeNode.build_binary_tree([1, 2])
assert Solution.diameterOfBinaryTree(root_test) == 1

print("All unit tests are passed")
