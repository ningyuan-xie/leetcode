"""563. Binary Tree Tilt
Link: https://leetcode.com/problems/binary-tree-tilt/
Difficulty: Easy
Description: Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left subtree node values
and all right subtree node values. If a node does not have a left child, then the sum of
the left subtree node, and vice versa, is treated as 0.
The sum of a leaf node is considered to be 0."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def findTilt(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           The trick is while calculating the sum, use sum to also get the tilt.
           Similar to 0543-Diameter-of-Binary-Tree.py"""

        def postorder_dfs_traversal(node):
            """Helper function to calculate tilt and sum of subtree"""
            if not node:  # A leaf node's node.left and node.right are both None and return 0, 0
                return 0, 0  # Base case: sum, tilt

            # 1. Recursive Case: Traverse the left subtree
            left_sum, left_tilt = postorder_dfs_traversal(node.left)
            # 2. Recursive Case: Traverse the right subtree
            right_sum, right_tilt = postorder_dfs_traversal(node.right)
            # 3. Root Case: Calculate current node's tilt, cumulative node's tilt, and cumulative sum
            current_tilt = abs(left_sum - right_sum)  # from sum
            cumulative_tilt = current_tilt + left_tilt + right_tilt
            cumulative_sum = left_sum + right_sum + node.val

            return cumulative_sum, cumulative_tilt

        # Start traversal from root
        _, overall_tilt = postorder_dfs_traversal(root)
        return overall_tilt


# Input: root = [1, 2, 3], Output: 1
root_test = TreeNode.build_binary_tree([1, 2, 3])
assert Solution.findTilt(root_test) == 1

# Input: root = [4, 2, 9, 3, 5, None, 7], Output: 15
root_test = TreeNode.build_binary_tree([4, 2, 9, 3, 5, None, 7])
assert Solution.findTilt(root_test) == 15

# Input: root = [21, 7, 14, 1, 1, 2, 2, 3, 3], Output: 9
root_test = TreeNode.build_binary_tree([21, 7, 14, 1, 1, 2, 2, 3, 3])
assert Solution.findTilt(root_test) == 9

print("All unit tests are passed.")
