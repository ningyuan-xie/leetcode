# Link: https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy
# Description: Given the roots of two binary trees root and subRoot, return true if there is a
# subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree could also be considered as a subtree of itself.

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Preorder DFS Traversal. Time Complexity: O(m * n), Space Complexity: O(m + n)
    @staticmethod
    def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function: Preorder DFS Traversal. Same as 0100-Same-Tree.py
        def is_same_tree(node1, node2):
            # Base Case
            if not node1 and not node2:
                return True
            # Base Case
            if not node1 or not node2:
                return False
            # Root Case and Recursive Case
            return (node1.val == node2.val
                    and is_same_tree(node1.left, node2.left)
                    and is_same_tree(node1.right, node2.right))

        # Helper function: Preorder DFS Traversal. Time Complexity: O(m * n), Space Complexity: O(m + n)
        def preorder_dfs_traversal(node):
            # Base Case
            if not node:
                return False
            # Root Case: Check if the current node and subRoot are the same tree
            if is_same_tree(node, subRoot):
                return True
            # Recursive Case: Check if the left or right subtree and subRoot are the same tree
            return (preorder_dfs_traversal(node.left)
                    or preorder_dfs_traversal(node.right))

        return preorder_dfs_traversal(root)


# Unit Test: Input: root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2], Output: True
root_test = TreeNode.build_binary_tree([3, 4, 5, 1, 2])
sub_root_test = TreeNode.build_binary_tree([4, 1, 2])
assert Solution.isSubtree(root_test, sub_root_test) is True

# Unit Test: Input: root = [3, 4, 5, 1, 2, None, None, None, None, 0], subRoot = [4, 1, 2], Output: False
root_test = TreeNode.build_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
sub_root_test = TreeNode.build_binary_tree([4, 1, 2])
assert Solution.isSubtree(root_test, sub_root_test) is False

# Unit Test: Input: root = [1, 2, 3], subRoot = [2], Output: True
root_test = TreeNode.build_binary_tree([1, 2, 3])
sub_root_test = TreeNode.build_binary_tree([2])
assert Solution.isSubtree(root_test, sub_root_test) is True

print("All unit tests are passed")
