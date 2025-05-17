"""653. Two Sum IV - Input is a BST
Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Difficulty: Easy
Description: Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def findTarget(root: Optional[TreeNode], k: int) -> bool:
        """Optimal Solution: Inorder DFS & Set. Time Complexity: O(n), Space Complexity: O(n)."""
        seen = set()
        
        def inorder(node: Optional[TreeNode]) -> bool:
            """Inorder DFS to traverse the BST."""
            # Base case
            if not node:
                return False
            
            # If the complement of the current node value is in the set, return True
            if k - node.val in seen:
                return True
            # Add the current node value to the set
            seen.add(node.val)
            
            # Recursively traverse the left and right subtrees
            return inorder(node.left) or inorder(node.right)
        
        return inorder(root)


def unit_tests():
    # Input: root = [5, 3, 6, 2, 4, None, 7], k = 9, Output: True
    root = TreeNode.build_binary_tree([5, 3, 6, 2, 4, None, 7])
    assert Solution.findTarget(root, 9) is True

    # Input: root = [5, 3, 6, 2, 4, None, 7], k = 28, Output: False
    root = TreeNode.build_binary_tree([5, 3, 6, 2, 4, None, 7])
    assert Solution.findTarget(root, 28) is False

    # Input: root = [2, 1, 3], k = 4, Output: True
    root = TreeNode.build_binary_tree([2, 1, 3])
    assert Solution.findTarget(root, 4) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
