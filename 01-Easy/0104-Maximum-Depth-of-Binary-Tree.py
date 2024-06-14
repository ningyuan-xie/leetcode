# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Description: Given the root of a binary tree, return its maximum depth.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        # Base case: if the tree root is None, return 0
        if not root:
            return 0
        # Recursive DFS traversal: return the maximum depth of the left and right subtrees
        else:
            return 1 + max(Solution.maxDepth(root.left),
                           Solution.maxDepth(root.right))

    # Helper function to print the maximum depth of the binary tree
    @staticmethod
    def printMaxDepth(root: Optional[TreeNode]):
        print(Solution.maxDepth(root))


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: 3
# The input [3,9,20,null,null,15,7] = serialized format of a binary tree using level order traversal
# where null = a path terminator where no node exists below
Solution.printMaxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))

# Unit Test: Input: root = [1,null,2], Output: 2
# The input [1,null,2] = serialized format of a binary tree using level order traversal
# where null = a path terminator where no node exists below
Solution.printMaxDepth(TreeNode(1, None, TreeNode(2)))

# Unit Test: Input: root = [], Output: 0
Solution.printMaxDepth(None)
print("All unit tests are passed")
