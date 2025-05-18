"""404. Sum of Left Leaves
Link: https://leetcode.com/problems/sum-of-left-leaves/
Difficulty: Easy
Description: Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        
        def preorder_dfs(node: Optional[TreeNode], is_left: bool) -> int:
            """Helper function to perform DFS and calculate the sum of left leaves."""
            # Base case: if the node is None, return 0
            if not node:
                return 0

            # If it's a leaf node and it's a left child, return its value
            if not node.left and not node.right and is_left:
                return node.val

            # Continue DFS on left and right children
            return preorder_dfs(node.left, True) + preorder_dfs(node.right, False)

        # Start DFS from the root node
        return preorder_dfs(root, False)


def unit_tests():
    # Input: root = [3,9,20,null,null,15,7], Output: 24
    root = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert Solution.sumOfLeftLeaves(root) == 24

    # Input: root = [1], Output: 0
    root = TreeNode.build_binary_tree([1])
    assert Solution.sumOfLeftLeaves(root) == 0

    # Input: root = [], Output: 0
    root = TreeNode.build_binary_tree([])
    assert Solution.sumOfLeftLeaves(root) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
