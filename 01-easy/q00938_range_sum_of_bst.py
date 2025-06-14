"""938. Range Sum of BST
Link: https://leetcode.com/problems/range-sum-of-bst/
Difficulty: Easy
Description: Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high]."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""

        def preorder_dfs_sum(node: Optional[TreeNode]) -> int:
            """Helper function to perform preorder DFS and calculate the sum of the node values."""
            # Base case: if the node is None, return 0
            if not node:
                return 0

            # If the node value is less than low, only check right subtree
            if node.val < low:
                return preorder_dfs_sum(node.right)

            # If the node value is greater than high, only check left subtree
            if node.val > high:
                return preorder_dfs_sum(node.left)

            # If the node value is in range, return the sum of the node value and the sum of the left and right subtrees
            return node.val + preorder_dfs_sum(node.left) + preorder_dfs_sum(node.right)

        # Return the sum of the node values
        return preorder_dfs_sum(root)


def unit_tests():
    # Input: root = [10,5,15,3,7,null,18], low = 7, high = 15, Output: 32
    root = TreeNode.build_binary_tree([10, 5, 15, 3, 7, None, 18])
    assert Solution.rangeSumBST(root, 7, 15) == 32

    # Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10, Output: 23
    root = TreeNode.build_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    assert Solution.rangeSumBST(root, 6, 10) == 23


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
