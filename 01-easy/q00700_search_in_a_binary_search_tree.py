"""700. Search in a Binary Search Tree
Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
Difficulty: Easy
Description: You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        if not root:
            return None
        if root.val == val:
            return root
        # BST Property: left < root < right
        if val < root.val:
            return Solution.searchBST(root.left, val)
        else:
            return Solution.searchBST(root.right, val)


def unit_tests():
    # Input: root = [4, 2, 7, 1, 3], val = 2, Output: [2, 1, 3]
    root = TreeNode.build_binary_tree([4, 2, 7, 1, 3])
    output = TreeNode.build_binary_tree([2, 1, 3])
    assert Solution.searchBST(root, 2) == output

    # Input: root = [4, 2, 7, 1, 3], val = 5, Output: None
    root = TreeNode.build_binary_tree([4, 2, 7, 1, 3])
    output = TreeNode.build_binary_tree([])
    assert Solution.searchBST(root, 5) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
