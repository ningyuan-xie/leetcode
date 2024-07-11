# Link: https://leetcode.com/problems/sum-of-left-leaves/
# Difficulty: Easy
# Description: Find the sum of all left leaves in a given binary tree.

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Recursive DFS. Time Complexity: O(n), Space Complexity: O(n)
    # Similar to 0101-Symmetric-Tree.py and 0257-Binary-Tree-Paths.py,
    # we need an inner helper DFS function to take two parameters
    @staticmethod
    def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
        # Initialize the sum of left leaves
        sum_left_leaves = 0
        # need to declare it as nonlocal since int is immutable (cannot change in place),
        # so modifications to the integer will not be reflected in the outer scope

        # Helper function: Depth-First Search
        def dfs(node: Optional[TreeNode], is_left: bool) -> None:
            # Base Case: If the node is None, return
            if not node:
                return
            # If the node is a leaf node and is on the left side, add its value to the sum
            if not node.left and not node.right and is_left:
                nonlocal sum_left_leaves  # nonlocal keyword to access the variable in the outer scope
                sum_left_leaves += node.val
            # Recursively traverse the left and right subtrees
            dfs(node=node.left, is_left=True)  # specify parameter name here to avoid confusion
            dfs(node=node.right, is_left=False)

        # Start the Depth-First Search
        dfs(node=root, is_left=False)  # current node is not on the left side
        return sum_left_leaves


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: 24
root_test = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert Solution.sumOfLeftLeaves(root_test) == 24

# Unit Test: Input: root = [1], Output: 0
root_test = TreeNode(1)
assert Solution.sumOfLeftLeaves(root_test) == 0

# Unit Test: Input: root = [], Output: 0
root_test = None
assert Solution.sumOfLeftLeaves(root_test) == 0

print("All unit tests are passed")
