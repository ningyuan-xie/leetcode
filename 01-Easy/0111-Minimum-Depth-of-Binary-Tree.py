# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Difficulty: Easy
# Description: Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def minDepth(root: Optional[TreeNode]) -> int:
        # Base case: if the tree root is None, return 0
        if not root:
            return 0
        # Recursive DFS traversal: return the minimum depth of the left and right subtrees
        else:
            left_depth = Solution.minDepth(root.left)
            right_depth = Solution.minDepth(root.right)
            # If either the left or right subtree is empty, return the non-empty subtree + 1
            # + 1 for the root node
            if not root.left or not root.right:
                return left_depth + right_depth + 1
            # Return the minimum depth of the left and right subtrees
            # + 1 for every time we go down a level
            return min(left_depth, right_depth) + 1


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: 2
assert Solution.minDepth(TreeNode(3,
                                  TreeNode(9), TreeNode(20,
                                                        TreeNode(15), TreeNode(7)))) == 2

# Unit Test: Input: root = [2,null,3,null,4,null,5,null,6], Output: 5
assert Solution.minDepth(TreeNode(2, None,
                                  TreeNode(3, None,
                                           TreeNode(4, None,
                                                    TreeNode(5, None, TreeNode(6)))))) == 5

# Unit Test: Input: root = [1,2], Output: 2
assert Solution.minDepth(TreeNode(1, TreeNode(2))) == 2

# Unit Test: Input: root = [1,null,2], Output: 2
assert Solution.minDepth(TreeNode(1, None, TreeNode(2))) == 2

# Unit Test: Input: root = [], Output: 0
assert Solution.minDepth(None) == 0
print("All unit tests are passed")
