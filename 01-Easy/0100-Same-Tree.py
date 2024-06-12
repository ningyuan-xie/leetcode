# Link: https://leetcode.com/problems/same-tree/
# Difficulty: Easy
# Description: Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both trees are None, then they are the same
        if not p and not q:
            return True
        # Base case: If one of the trees is None, then they are not the same
        if not p or not q:
            return False
        # Base case: If the values of the roots are not the same, then they are not the same
        if p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return (Solution.isSameTree(p.left, q.left) and
                Solution.isSameTree(p.right, q.right))


# Unit Test: Input: p = [1,2,3], q = [1,2,3], Output: True
# The input [1,2,3] = serialized format of a binary tree using level order traversal
assert Solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)),
                           TreeNode(1, TreeNode(2), TreeNode(3))) == True

# Unit Test: Input: p = [1,2], q = [1,null,2], Output: False
# The input [1,2] = serialized format of a binary tree using level order traversal
assert Solution.isSameTree(TreeNode(1, TreeNode(2)),
                           TreeNode(1, None, TreeNode(2))) == False

# Unit Test: Input: p = [1,2,1], q = [1,1,2], Output: False
# The input [1,2,1] = serialized format of a binary tree using level order traversal
assert Solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)),
                           TreeNode(1, TreeNode(1), TreeNode(2))) == False
print("All unit tests are passed")
