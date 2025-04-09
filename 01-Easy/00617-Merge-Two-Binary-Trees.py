"""617. Merge Two Binary Trees
Link: https://leetcode.com/problems/merge-two-binary-trees/
Difficulty: Easy
Description: You are given two binary trees root1 and root2. Imagine that when you put one of
them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of
the merged node. Otherwise, the NOT null node will be used as the node of the new tree."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)"""
        # Base case: If both trees are empty
        if not root1 and not root2:
            return None
        # Base case: If one of the trees is empty, return the other tree
        if not root1:
            return root2
        if not root2:
            return root1

        # Root Case: Sum the node values of the two
        root1.val += root2.val
        # Recursive Case: Merge the left and right subtrees
        root1.left = Solution.mergeTrees(root1.left, root2.left)
        root1.right = Solution.mergeTrees(root1.right, root2.right)
        return root1


# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7], Output: [3,4,5,5,4,null,7]
root_test1 = TreeNode.build_binary_tree([1, 3, 2, 5])
root_test2 = TreeNode.build_binary_tree([2, 1, 3, None, 4, None, 7])
root_expected = TreeNode.build_binary_tree([3, 4, 5, 5, 4, None, 7])
assert Solution.mergeTrees(root_test1, root_test2) == root_expected

# Input: root1 = [1], root2 = [1, 2], Output: [2, 2]
root_test1 = TreeNode.build_binary_tree([1])
root_test2 = TreeNode.build_binary_tree([1, 2])
root_expected = TreeNode.build_binary_tree([2, 2])
assert Solution.mergeTrees(root_test1, root_test2) == root_expected

# Input: root1 = [1, 2, 3], root2 = [1, 2, 3], Output: [2, 4, 6]
root_test1 = TreeNode.build_binary_tree([1, 2, 3])
root_test2 = TreeNode.build_binary_tree([1, 2, 3])
root_expected = TreeNode.build_binary_tree([2, 4, 6])
assert Solution.mergeTrees(root_test1, root_test2) == root_expected

print("All unit tests are passed.")
