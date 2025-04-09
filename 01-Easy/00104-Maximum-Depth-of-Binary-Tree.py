"""104. Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Description: Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node = height of the tree + 1"""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Postorder because we need to traverse the left and right subtrees first before the root"""
        # Base case: if the tree root is None, return 0
        if not root:
            return 0
        # 1. Recursive Case: Traverse the left subtree
        left_depth = Solution.maxDepth(root.left)
        # 2. Recursive Case: Traverse the right subtree
        right_depth = Solution.maxDepth(root.right)
        # 3. Root Case: Return the maximum depth of the left and right subtrees
        # + 1 to account for the current node
        root_depth = max(left_depth, right_depth) + 1

        return root_depth


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: 3
# The input [3,9,20,null,null,15,7] = serialized format of a binary tree using level order traversal
# where null = a path terminator where no node exists below
root_test = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
assert Solution.maxDepth(root_test) == 3

# Unit Test: Input: root = [1,null,2], Output: 2
# The input [1,null,2] = serialized format of a binary tree using level order traversal
# where null = a path terminator where no node exists below
root_test = TreeNode.build_binary_tree([1, None, 2])
assert Solution.maxDepth(root_test) == 2

# Unit Test: Input: root = [], Output: 0
root_test = TreeNode.build_binary_tree([])
assert Solution.maxDepth(root_test) == 0

print("All unit tests are passed")
