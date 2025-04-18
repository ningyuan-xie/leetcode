"""100. Same Tree
Link: https://leetcode.com/problems/same-tree/
Difficulty: Easy
Description: Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case: If both trees are None, return True
        if not p and not q:
            return True
        # Base Case: If one tree is None and the other is not, return False
        if not p or not q:
            return False
        # Recursive Case: root -> left -> right
        return (p.val == q.val and 
                Solution.isSameTree(p.left, q.left) and 
                Solution.isSameTree(p.right, q.right))


def unit_tests():
    # Input: p = [1,2,3], q = [1,2,3], Output: True
    p = TreeNode.build_binary_tree([1, 2, 3])
    q = TreeNode.build_binary_tree([1, 2, 3])
    assert Solution.isSameTree(p, q) is True

    # Input: p = [1,2], q = [1,null,2], Output: False
    p = TreeNode.build_binary_tree([1, 2])
    q = TreeNode.build_binary_tree([1, None, 2])
    assert Solution.isSameTree(p, q) is False

    # Input: p = [1,2,1], q = [1,1,2], Output: False
    p = TreeNode.build_binary_tree([1, 2, 1])
    q = TreeNode.build_binary_tree([1, 1, 2])
    assert Solution.isSameTree(p, q) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
