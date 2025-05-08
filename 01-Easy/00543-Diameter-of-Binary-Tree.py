"""543. Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Difficulty: Easy
Description: Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS. Time Complexity: O(n), Space Complexity: O(n).
        Similar to 104. Maximum Depth of Binary Tree."""
        max_diameter = 0

        def postorder(node: Optional[TreeNode]) -> int:
            """Helper function to calculate the depth of each subtree and update the maximum diameter."""
            nonlocal max_diameter
            if not node:
                return 0
            
            left_depth = postorder(node.left)
            right_depth = postorder(node.right)
            
            # Update the maximum diameter found so far
            max_diameter = max(max_diameter, left_depth + right_depth)
            
            # Return the depth of the current node
            return max(left_depth, right_depth) + 1
            
        postorder(root)
        return max_diameter


def unit_tests():
    # Input: root = [1, 2, 3, 4, 5], Output: 3
    root = TreeNode.build_binary_tree([1, 2, 3, 4, 5])
    assert Solution.diameterOfBinaryTree(root) == 3

    # Input: root = [1, 2], Output: 1
    root = TreeNode.build_binary_tree([1, 2])
    assert Solution.diameterOfBinaryTree(root) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
