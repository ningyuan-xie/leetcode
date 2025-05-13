"""617. Merge Two Binary Trees
Link: https://leetcode.com/problems/merge-two-binary-trees/
Difficulty: Easy
Description: You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base case: If one of the trees is empty, return the other tree
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        # Create new node with sum of values
        merged = TreeNode(root1.val + root2.val)
        # Recursively merge left and right subtrees
        merged.left = Solution.mergeTrees(root1.left, root2.left)
        merged.right = Solution.mergeTrees(root1.right, root2.right)
        
        return merged


def unit_test():
    # Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7], Output: [3,4,5,5,4,null,7]
    root1 = TreeNode.build_binary_tree([1, 3, 2, 5])
    root2 = TreeNode.build_binary_tree([2, 1, 3, None, 4, None, 7])
    output = TreeNode.build_binary_tree([3, 4, 5, 5, 4, None, 7])
    assert Solution.mergeTrees(root1, root2) == output

    # Input: root1 = [1], root2 = [1, 2], Output: [2, 2]
    root1 = TreeNode.build_binary_tree([1])
    root2 = TreeNode.build_binary_tree([1, 2])
    output = TreeNode.build_binary_tree([2, 2])
    assert Solution.mergeTrees(root1, root2) == output

    # Input: root1 = [1, 2, 3], root2 = [1, 2, 3], Output: [2, 4, 6]
    root1 = TreeNode.build_binary_tree([1, 2, 3])
    root2 = TreeNode.build_binary_tree([1, 2, 3])
    output = TreeNode.build_binary_tree([2, 4, 6])
    assert Solution.mergeTrees(root1, root2) == output


if __name__ == "__main__":
    unit_test()
    print("All unit tests are passed.")
