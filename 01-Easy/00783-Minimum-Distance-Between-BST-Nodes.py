"""783. Minimum Distance Between BST Nodes
Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
Difficulty: Easy
Description: Given the root of a Binary Search Tree (BST), return the minimum difference between
the values of any two different nodes in the tree."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def minDiffInBST(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Inorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Same as 0530-Minimum-Absolute-Difference-in-BST.py"""
        # Initialize the minimum absolute difference
        min_absolute_diff = float("inf")  # positive infinity
        # Initialize the previous node
        prev_node: Optional[TreeNode] = None

        def inorder_dfs_traversal(node: TreeNode) -> None:
            """Helper function: Inorder DFS Traversal: left -> root -> right
               Inorder because for BST, the inorder traversal will be in ascending order,
               which allows us to find the minimum absolute difference in a single traversal"""
            # nonlocal variables to access the outer scope immutable variables
            nonlocal min_absolute_diff, prev_node
            # Base Case: If the current node is None, do nothing and return
            if not node:
                return
            # Recursive inorder DFS traversal: left -> root -> right
            # 1. Recursive Case: Traverse the left subtree
            inorder_dfs_traversal(node.left)
            # 2. Root Case: Process the current node
            if prev_node:
                # Update the minimum absolute difference
                min_absolute_diff = min(min_absolute_diff, node.val - prev_node.val)
            # Update prev_node to node not node.val,
            # otherwise, "if prev_node:" above will be False when prev_node = 0;
            # alternatively, we can also use "if prev_node is not None:" to avoid this issue
            prev_node = node
            # 3. Recursive Case: Traverse the right subtree
            inorder_dfs_traversal(node.right)

        # Perform inorder traversal
        inorder_dfs_traversal(root)
        return int(min_absolute_diff)


# Unit Test: Input: root = [4, 2, 6, 1, 3], Output: 1
# root_test = TreeNode.build_binary_tree([4, 2, 6, 1, 3])
# assert Solution.minDiffInBST(root_test) == 1
#
# # Unit Test: Input: root = [1, 0, 48, None, None, 12, 49], Output: 1
# root_test = TreeNode.build_binary_tree([1, 0, 48, None, None, 12, 49])
# assert Solution.minDiffInBST(root_test) == 1
#
# # Unit Test: Input: root = [1, None, 5, 3], Output: 2
# root_test = TreeNode.build_binary_tree([1, None, 5, 3])
# assert Solution.minDiffInBST(root_test) == 2

# Unit Test: Input: root = [0,null,2236,1277,2776,519], Output: 519
root_test = TreeNode.build_binary_tree([0, None, 2236, 1277, 2776, 519])
assert Solution.minDiffInBST(root_test) == 519

print("All unit tests are passed")
