# Link: https://leetcode.com/problems/symmetric-tree/
# Difficulty: Easy
# Description: Given the root of a binary tree,
# check whether it is a mirror of itself (i.e., symmetric around its center).

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Recursive DFS. Time Complexity: O(n), Space Complexity: O(n)
    # Similar to 0100-Same-Tree.py, we need an inner helper DFS function to take two parameters
    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:  # only takes one parameter root
        # However, we need to compare the left and right subtrees simultaneously
        # Therefore, need an inner helper DFS function (like isSameTree) to take two parameters
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Base case: if both trees are None, then they are the same
            if not left and not right:
                return True
            # Base case: If one of the trees is None, then they are not the same
            if not left or not right:
                return False
            # Base case: If the values of the roots are not the same, then they are not the same
            if left.val != right.val:
                return False
            # DFS: Recursively check the left and right subtrees
            return (dfs(left.left, right.right) and
                    dfs(left.right, right.left))
        # Start the DFS traversal
        return dfs(root.left, root.right)


# Unit Test: Input: root = [1,2,2,3,4,4,3], Output: True
# The input [1,2,2,3,4,4,3] = serialized format of a binary tree using level order traversal
assert Solution.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                                     TreeNode(2, TreeNode(4), TreeNode(3)))) == True

print("All unit tests are passed")
