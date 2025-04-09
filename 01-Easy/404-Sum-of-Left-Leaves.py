"""404. Sum of Left Leaves
Link: https://leetcode.com/problems/sum-of-left-leaves/
Difficulty: Easy
Description: Find the sum of all left leaves in a given binary tree."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0101-Symmetric-Tree.py and 0257-Binary-Tree-Paths.py,
           we need an inner helper DFS function to take two parameters"""
        # Initialize the sum of left leaves
        sum_left_leaves = 0
        # need to declare it as nonlocal since int is immutable (cannot change in place),
        # so modifications to the integer will not be reflected in the outer scope

        def preorder_dfs_path(node: Optional[TreeNode], is_left: bool) -> None:
            """Helper function: Preorder DFS Traversal: root -> left -> right
               Preorder because we want to process the current node first"""
            # Base Case: If the node is None, return
            if not node:
                return
            # 1. Root Case: If the node is a leaf node and is on the left side, add its value to sum
            if not node.left and not node.right and is_left:
                nonlocal sum_left_leaves  # nonlocal keyword to access the variable in the outer scope
                sum_left_leaves += node.val
            # 2. Recursive Case: Traverse the left subtree
            preorder_dfs_path(node=node.left, is_left=True)  # specify parameter name here
            # 3. Recursive Case: Traverse the right subtree
            preorder_dfs_path(node=node.right, is_left=False)

        # Perform preorder DFS traversal from the root
        preorder_dfs_path(node=root, is_left=False)  # current node is not on the left side
        return sum_left_leaves


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: 24
root_test = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
assert Solution.sumOfLeftLeaves(root_test) == 24

# Unit Test: Input: root = [1], Output: 0
root_test = TreeNode.build_binary_tree([1])
assert Solution.sumOfLeftLeaves(root_test) == 0

# Unit Test: Input: root = [], Output: 0
root_test = TreeNode.build_binary_tree([])
assert Solution.sumOfLeftLeaves(root_test) == 0

print("All unit tests are passed")
