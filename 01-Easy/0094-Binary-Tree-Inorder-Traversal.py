# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Difficulty: Easy
# Description: Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        # Base case: if the tree root is None, return an empty list
        if not root:
            return []
        # Recursive inorder DFS traversal: left -> root -> right
        # For BST, this will be in ascending order
        else:
            return (Solution.inorderTraversal(root.left) +
                    [root.val] +
                    Solution.inorderTraversal(root.right))


# Unit Test: Input: root = [1,null,2,3], Output: [1,3,2]
# The input [1,null,2,3] = serialized format of a binary tree using level order traversal,
# where null = a path terminator where no node exists below
assert Solution.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 3, 2]

# Unit Test: Input: root = [], Output: []
assert Solution.inorderTraversal(None) == []

# Unit Test: Input: root = [1], Output: [1]
assert Solution.inorderTraversal(TreeNode(1)) == [1]
print("All unit tests are passed")
