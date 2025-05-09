"""572. Subtree of Another Tree
Link: https://leetcode.com/problems/subtree-of-another-tree/
Difficulty: Easy
Description: Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(m*n), Space Complexity: O(m).
        Similar to 100. Same Tree."""
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            """Helper function to check if two trees are identical."""
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (p.val == q.val 
                    and isSameTree(p.left, q.left) 
                    and isSameTree(p.right, q.right))
        
        def preorder(node: Optional[TreeNode]) -> bool:
            """Helper function to traverse main tree and check for subtree match."""
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            return preorder(node.left) or preorder(node.right)
            
        return preorder(root)


def unit_tests():
    # Input: root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2], Output: True
    root = TreeNode.build_binary_tree([3, 4, 5, 1, 2])
    subRoot = TreeNode.build_binary_tree([4, 1, 2])
    assert Solution.isSubtree(root, subRoot) is True

    # Input: root = [3, 4, 5, 1, 2, None, None, None, None, 0], subRoot = [4, 1, 2], Output: False
    root = TreeNode.build_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = TreeNode.build_binary_tree([4, 1, 2])
    assert Solution.isSubtree(root, subRoot) is False

    # Input: root = [1, 2, 3], subRoot = [2], Output: True
    root = TreeNode.build_binary_tree([1, 2, 3])
    subRoot = TreeNode.build_binary_tree([2])
    assert Solution.isSubtree(root, subRoot) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
