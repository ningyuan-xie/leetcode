"""112. Path Sum
Link: https://leetcode.com/problems/path-sum/
Difficulty: Easy
Description: Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case: If the tree is empty, return False
        if not root:
            return False

        # Check if we are at a leaf node and if the current value equals targetSum
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursive Case: Check both left and right subtrees with the updated targetSum
        targetSum -= root.val
        return Solution.hasPathSum(root.left, targetSum) or Solution.hasPathSum(root.right, targetSum)


def unit_tests():
    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22, Output: True
    root = TreeNode.build_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    assert Solution.hasPathSum(root, 22) is True

    # Input: root = [1,2,3], targetSum = 5, Output: False
    root = TreeNode.build_binary_tree([1, 2, 3])
    assert Solution.hasPathSum(root, 5) is False

    # Input: root = [1,2], targetSum = 0, Output: False
    root = TreeNode.build_binary_tree([1, 2])
    assert Solution.hasPathSum(root, 0) is False

    # Input: root = [], targetSum = 0, Output: False
    root = None
    assert Solution.hasPathSum(root, 0) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
