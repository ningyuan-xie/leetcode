"""104. Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Description: Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case: If the tree is empty, return 0
        if not root:
            return 0
        
        # Return the maximum of the two depths plus one for the current node
        return max(Solution.maxDepth(root.left), Solution.maxDepth(root.right)) + 1


def unit_tests():
    # Input: root = [3,9,20,null,null,15,7], Output: 3
    root = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert Solution.maxDepth(root) == 3

    # Input: root = [1,null,2], Output: 2
    root = TreeNode.build_binary_tree([1, None, 2])
    assert Solution.maxDepth(root) == 2

    # Input: root = [], Output: 0
    root = TreeNode.build_binary_tree([])
    assert Solution.maxDepth(root) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
