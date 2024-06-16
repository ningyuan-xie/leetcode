# Link: https://leetcode.com/problems/balanced-binary-tree/
# Difficulty: Easy
# Description: Given a binary tree, determine if it is height-balanced.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isBalanced(root: Optional[TreeNode]) -> bool:
        # Helper function 1 to calculate the height of the tree
        # Similar to 0104-Maximum-Depth-of-Binary-Tree.py
        def height(node: Optional[TreeNode]) -> int:
            # Base case: if the node is None, height is -1
            if not node:
                return -1
            # Recursively calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            # Return the maximum height of the left and right subtrees
            # + 1 for every time we go down a level
            return max(left_height, right_height) + 1

        # Helper function 2 to check if the tree is balanced
        def is_balanced(node: Optional[TreeNode]) -> bool:
            # Base case: if the node is None, return True
            if not node:
                return True
            # Recursively check if the left and right subtrees are balanced
            left_balanced = is_balanced(node.left)
            right_balanced = is_balanced(node.right)
            # If either subtree is not balanced, return False
            if not left_balanced or not right_balanced:
                return False
            # Check if the difference in height between the left and right subtrees <= 1
            if abs(height(node.left) - height(node.right)) > 1:
                return False
            # If both conditions are met, return True
            return True

        # Call the helper function to check if the tree is balanced
        return is_balanced(root)


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: True
# The input [3,9,20,null,null,15,7] = serialized format of a binary tree using level order traversal,
# where null = a path terminator where no node exists below
# The tree is balanced with height difference of 1
assert Solution.isBalanced(TreeNode(3, TreeNode(9),
                                    TreeNode(20, TreeNode(15), TreeNode(7)))) == True

# Unit Test: Input: root = [1,2,2,3,3,null,null,4,4], Output: False
# The input [1,2,2,3,3,null,null,4,4] = serialized format of a binary tree using level order traversal,
# where null = a path terminator where no node exists below
# The tree is not balanced with height difference of 2
assert Solution.isBalanced(
    TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)),
                         TreeNode(3)), TreeNode(2))) == False

# Unit Test: Input: root = [], Output: True
# An empty tree is considered balanced
assert Solution.isBalanced(None) == True

# Unit Test: Input: root = [1], Output: True
# A single node tree is considered balanced
assert Solution.isBalanced(TreeNode(1)) == True
print("All unit tests are passed")
