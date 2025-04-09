"""671. Second Minimum Node In a Binary Tree
Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
Difficulty: Easy
Description: Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then
this node's value is the smaller value among its two sub-nodes. More formally, the property
root.val = min(root.left.val, root.right.val) always holds.
Given such a binary tree, you need to output the second minimum value in the set made of all the
nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)"""

        def preorder(node: Optional[TreeNode]) -> None:
            """Helper function: Preorder DFS to find the second minimum value"""
            if node is None:
                return

            # Check if the current node has a value greater than the minimum value
            # root.val is always the minimum value according to description
            if root.val < node.val < second_min[0]:
                second_min[0] = node.val
            preorder(node.left)
            preorder(node.right)

        # Initialize the second minimum value
        second_min = [float('inf')]  # Initialize with infinity
        preorder(root)
        return -1 if second_min[0] == float('inf') else second_min[0]


# Unit Test: Input: root = [2, 2, 5, None, None, 5, 7], Output: 5
root_test = TreeNode.build_binary_tree([2, 2, 5, None, None, 5, 7])
assert Solution.findSecondMinimumValue(root_test) == 5

# Unit Test: Input: root = [2, 2, 2], Output: -1
root_test = TreeNode.build_binary_tree([2, 2, 2])
assert Solution.findSecondMinimumValue(root_test) == -1

# Unit Test: Input: root = [2, 2, 2, 2, 2, 2, 2], Output: -1
root_test = TreeNode.build_binary_tree([2, 2, 2, 2, 2, 2, 2])
assert Solution.findSecondMinimumValue(root_test) == -1

print("All unit tests are passed")
