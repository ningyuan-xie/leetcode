"""2236. Root Equals Sum of Children
Link: https://leetcode.com/problems/root-equals-sum-of-children/
Difficulty: Easy
Description: You are given the root of a binary tree that consists of exactly 3 nodes: the root,
its left child, and its right child.
Return true if the value of the root is equal to the sum of the values of its two children, or
false otherwise."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isSumEqual(root: Optional[TreeNode]) -> bool:
        """Optimal Solution: Subtree Sum. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base case: If the root is None, return False
        if root is None:
            return False

        return root.val == (root.left.val + root.right.val)


# Input: root = [10,4,6], Output: True
root_test = TreeNode.build_binary_tree([10, 4, 6])
assert Solution.isSumEqual(root_test) is True

# Input: root = [5,3,1], Output: False
root_test = TreeNode.build_binary_tree([5, 3, 1])
assert Solution.isSumEqual(root_test) is False

print("All unit tests are passed.")
