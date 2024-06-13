# Link: https://leetcode.com/problems/symmetric-tree/
# Difficulty: Easy
# Description: Given the root of a binary tree,
# check whether it is a mirror of itself (i.e., symmetric around its center).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            # Base case: if both trees are None, then they are the same
            if not left and not right:
                return True
            # Base case: If one of the trees is None, then they are not the same
            if not left or not right:
                return False
            # Recursive case: if the values of the roots are the same
            # and the left subtree of the left tree is the mirror of the right subtree of the right tree
            # and the right subtree of the left tree is the mirror of the left subtree of the right tree
            return (left.val == right.val and
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left))

        # Start the DFS traversal
        return dfs(root.left, root.right)


# Unit Test: Input: root = [1,2,2,3,4,4,3], Output: True
# The input [1,2,2,3,4,4,3] = serialized format of a binary tree using level order traversal
assert Solution.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                                     TreeNode(2, TreeNode(4), TreeNode(3)))) == True
print("All unit tests are passed")
