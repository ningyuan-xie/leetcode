"""1022. Sum of Root To Leaf Binary Numbers
Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
Difficulty: Easy
Description: You are given the root of a binary tree where each node has a value 0 or 1.
Each root-to-leaf path represents a binary number starting with the most significant bit.
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary,
which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.
The test cases are generated so that the answer fits in a 32-bits integer."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def sumRootToLeaf(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(h).
           Similar to 1018-Binary-Prefix-Divisible-By-5.py"""

        def preorder_dfs(node: Optional[TreeNode], current_sum: int) -> int:
            """Helper function to perform preorder DFS"""
            # If the node is None, return 0
            if not node:
                return 0

            # Update the current sum; (current_sum << 1) is equivalent current_sum * 2
            current_sum = (current_sum << 1) + node.val

            # If it's a leaf node, return the current sum
            if not node.left and not node.right:
                return current_sum

            # Otherwise, return the sum of the left and right subtrees
            return preorder_dfs(node.left, current_sum) + preorder_dfs(node.right, current_sum)

        return preorder_dfs(root, 0)


# Unit Test: root = [1, 0, 1, 0, 1, 0, 1], Output: 22
root_test = TreeNode.build_binary_tree([1, 0, 1, 0, 1, 0, 1])
assert Solution.sumRootToLeaf(root_test) == 22

# Unit Test: root = [1, 1, 0, 0, 1, 0, 1], Output: 22
root_test = TreeNode.build_binary_tree([1, 1, 0, 0, 1, 0, 1])
assert Solution.sumRootToLeaf(root_test) == 22

# Unit Test: root = [1], Output: 1
root_test = TreeNode.build_binary_tree([1])
assert Solution.sumRootToLeaf(root_test) == 1

print("All unit tests are passed.")
