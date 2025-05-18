"""110. Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree/
Difficulty: Easy
Description: Given a binary tree, determine if it is height-balanced."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isBalanced(root: Optional[TreeNode]) -> bool:
        """Optimal Solution: Postorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""

        def is_balanced(node: Optional[TreeNode]) -> int:
            """Postorder DFS to check if the tree is balanced."""
            # Base Case: If the node is None, return height -1
            if not node:
                return -1
            
            # Recursive Case: Check the left and right subtrees
            left = is_balanced(node.left)
            right = is_balanced(node.right)

            # If already imbalanced, propagate the error code (-2)
            if left == -2 or right == -2 or abs(left - right) > 1:
                return -2

            # If still balanced, return the height of the tree
            return max(left, right) + 1

        return is_balanced(root) != -2
    

def unit_tests():
    # Input: root = [3,9,20,null,null,15,7], Output: True
    root = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert Solution.isBalanced(root) is True

    # Input: root = [1,2,2,3,3,null,null,4,4], Output: False
    root = TreeNode.build_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert Solution.isBalanced(root) is False

    # Input: root = [], Output: True. An empty tree is considered balanced
    root = TreeNode.build_binary_tree([])
    assert Solution.isBalanced(root) is True

    # Input: root = [1], Output: True. A single node tree is considered balanced
    root = TreeNode.build_binary_tree([1])
    assert Solution.isBalanced(root) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
