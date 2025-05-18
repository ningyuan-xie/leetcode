"""783. Minimum Distance Between BST Nodes
Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
Difficulty: Easy
Description: Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def minDiffInBST(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Inorder DFS. Time Complexity: O(n), Space Complexity: O(n).
        Same as 530. Minimum Absolute Difference in BST."""
        # Initialize min difference and previous node
        min_diff = float('inf')
        prev = None
        
        def inorder(node: Optional[TreeNode]) -> None:
            """Helper function to traverse BST nodes in sorted order, allowing min difference to be found by comparing adjacent nodes."""
            nonlocal min_diff, prev
            if not node:
                return
            
            inorder(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node
            inorder(node.right)
        
        inorder(root)
        return min_diff


def unit_tests():
    # Input: root = [4, 2, 6, 1, 3], Output: 1
    root = TreeNode.build_binary_tree([4, 2, 6, 1, 3])
    assert Solution.minDiffInBST(root) == 1

    # Input: root = [1, 0, 48, None, None, 12, 49], Output: 1
    root = TreeNode.build_binary_tree([1, 0, 48, None, None, 12, 49])
    assert Solution.minDiffInBST(root) == 1

    # Input: root = [1, None, 5, 3], Output: 2
    root = TreeNode.build_binary_tree([1, None, 5, 3])
    assert Solution.minDiffInBST(root) == 2

    # Input: root = [0,null,2236,1277,2776,519], Output: 519
    root = TreeNode.build_binary_tree([0, None, 2236, 1277, 2776, 519])
    assert Solution.minDiffInBST(root) == 519


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
