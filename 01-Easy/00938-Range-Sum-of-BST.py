"""938. Range Sum of BST
Link: https://leetcode.com/problems/range-sum-of-bst/
Difficulty: Easy
Description: Given the root node of a binary search tree, return the sum of values of all nodes with
a value in the range [low, high]."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)."""

        def preorder_dfs_sum(node: Optional[TreeNode]) -> int:
            """Helper Function: Preorder DFS Traversal to calculate the sum of the node values;
               note that this function initializes sum_value within and returns the sum_value"""
            # Return 0 if the node is None
            if not node:
                return 0
            # Initialize the sum to 0
            sum_value = 0

            # If the node value is within the range, add it to the sum
            if low <= node.val <= high:
                sum_value += node.val

            # If the node value is greater than the low value, traverse the left subtree
            if node.val > low:
                sum_value += preorder_dfs_sum(node.left)

            # If the node value is less than the high value, traverse the right subtree
            if node.val < high:
                sum_value += preorder_dfs_sum(node.right)

            # Return the sum of the node values
            return sum_value

        # Return the sum of the node values
        return preorder_dfs_sum(root)

    @staticmethod
    def rangeSumBSTnonlocal(root: Optional[TreeNode], low: int, high: int) -> int:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 0404-Sum-of-Left-Leaves.py"""
        # Initialize the sum to 0
        sum_value = 0

        def preorder_dfs_sum_nonlocal(node: Optional[TreeNode]) -> None:
            """Helper Function: Preorder DFS Traversal to calculate the sum of the node values;
               note that this function uses nonlocal to access the sum_value and return None"""
            # Return if the node is None
            if not node:
                return
            nonlocal sum_value

            # If the node value is within the range, add it to the sum
            if low <= node.val <= high:
                sum_value += node.val

            # If the node value is greater than the low value, traverse the left subtree
            if node.val > low:
                preorder_dfs_sum_nonlocal(node.left)

            # If the node value is less than the high value, traverse the right subtree
            if node.val < high:
                preorder_dfs_sum_nonlocal(node.right)

        # Return the sum of the node values
        preorder_dfs_sum_nonlocal(root)
        return sum_value


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15, Output: 32
root_test = TreeNode.build_binary_tree([10, 5, 15, 3, 7, None, 18])
assert Solution.rangeSumBST(root_test, 7, 15) == 32

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10, Output: 23
root_test = TreeNode.build_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
assert Solution.rangeSumBSTnonlocal(root_test, 6, 10) == 23

print("All unit tests are passed.")
