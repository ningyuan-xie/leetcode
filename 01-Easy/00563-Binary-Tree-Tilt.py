"""563. Binary Tree Tilt
Link: https://leetcode.com/problems/binary-tree-tilt/
Difficulty: Easy
Description: Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def findTilt(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        total_tilt = 0

        def postorder(node: Optional[TreeNode]) -> int:
            """Helper function to calculate subtree sums and accumulate tilt."""
            nonlocal total_tilt
            if not node:
                return 0
            
            left_sum = postorder(node.left)
            right_sum = postorder(node.right)
            
            # Calculate current node's tilt and add to total
            total_tilt += abs(left_sum - right_sum)
            
            # Return sum of current subtree
            return node.val + left_sum + right_sum
            
        postorder(root)
        return total_tilt


def unit_tests():
    # Input: root = [1, 2, 3], Output: 1
    root = TreeNode.build_binary_tree([1, 2, 3])
    assert Solution.findTilt(root) == 1

    # Input: root = [4, 2, 9, 3, 5, None, 7], Output: 15
    root = TreeNode.build_binary_tree([4, 2, 9, 3, 5, None, 7])
    assert Solution.findTilt(root) == 15

    # Input: root = [21, 7, 14, 1, 1, 2, 2, 3, 3], Output: 9
    root = TreeNode.build_binary_tree([21, 7, 14, 1, 1, 2, 2, 3, 3])
    assert Solution.findTilt(root) == 9


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
