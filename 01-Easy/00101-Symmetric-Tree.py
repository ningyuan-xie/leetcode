"""101. Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/
Difficulty: Easy
Description: Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center)."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0100-Same-Tree.py, we need an inner helper DFS function to take two parameters.
           This function only takes one parameter root, but we need to compare the left and right
           subtrees simultaneously. Therefore, we need an inner helper DFS function (like isSameTree)
           to take two parameters"""

        def preorder_dfs_traversal(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            """Helper DFS function to traverse the left and right subtrees simultaneously.
               Preorder because we need to compare the roots first before the subtrees"""
            # Base case: if both trees are None, then they are the same
            if not left and not right:
                return True
            # Base case: If one of the trees is None, then they are not the same
            if not left or not right:
                return False
            # 1. Root Case: If the values of the roots are not the same, then they are not the same
            root_same = left.val == right.val
            # 2. Recursive Case: Traverse the left subtrees
            left_same = preorder_dfs_traversal(left.left, right.right)
            # 3. Recursive Case: Traverse the right subtrees
            right_same = preorder_dfs_traversal(left.right, right.left)

            # Return the result of the recursive cases
            return root_same and left_same and right_same

        # Start the preorder traversal
        return preorder_dfs_traversal(root.left, root.right)


# Input: root = [1,2,2,3,4,4,3], Output: True
# The input [1,2,2,3,4,4,3] = serialized format of a binary tree using level order traversal
root_test = TreeNode.build_binary_tree([1, 2, 2, 3, 4, 4, 3])
assert Solution.isSymmetric(root_test) is True

print("All unit tests are passed.")
