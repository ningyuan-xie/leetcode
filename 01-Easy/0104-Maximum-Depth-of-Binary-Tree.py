# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Description: Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node. (!= height of the tree)

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Recursive DFS. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        # Base case: if the tree root is None, return 0
        if not root:
            return 0
        # Recursive DFS traversal: return the maximum depth of the left and right subtrees
        # + 1 for every time we go down a level
        left_depth = Solution.maxDepth(root.left)
        right_depth = Solution.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: 3
# The input [3,9,20,null,null,15,7] = serialized format of a binary tree using level order traversal
# where null = a path terminator where no node exists below
assert Solution.maxDepth(TreeNode(3,
                                  TreeNode(9), TreeNode(20,
                                                        TreeNode(15), TreeNode(7)))) == 3

# Unit Test: Input: root = [1,null,2], Output: 2
# The input [1,null,2] = serialized format of a binary tree using level order traversal
# where null = a path terminator where no node exists below
assert Solution.maxDepth(TreeNode(1, None, TreeNode(2))) == 2

# Unit Test: Input: root = [], Output: 0
assert Solution.maxDepth(None) == 0

print("All unit tests are passed")
