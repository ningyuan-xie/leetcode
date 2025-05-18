"""671. Second Minimum Node In a Binary Tree
Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
Difficulty: Easy
Description: Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # The root value is the minimum value in the tree (property of special binary tree)
        min_val = root.val
        second_min = float('inf')
        
        def preorder(node: Optional[TreeNode]) -> None:
            """Helper function to traverse the tree in preorder."""
            nonlocal second_min
            if not node:
                return
            # Early termination if node value is larger than current second_min
            if node.val > second_min:
                return
            if min_val < node.val < second_min:
                second_min = node.val
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return second_min if second_min != float('inf') else -1


def unit_tests():
    # Input: root = [2, 2, 5, None, None, 5, 7], Output: 5
    root = TreeNode.build_binary_tree([2, 2, 5, None, None, 5, 7])
    assert Solution.findSecondMinimumValue(root) == 5

    # Input: root = [2, 2, 2], Output: -1
    root = TreeNode.build_binary_tree([2, 2, 2])
    assert Solution.findSecondMinimumValue(root) == -1

    # Input: root = [2, 2, 2, 2, 2, 2, 2], Output: -1
    root = TreeNode.build_binary_tree([2, 2, 2, 2, 2, 2, 2])
    assert Solution.findSecondMinimumValue(root) == -1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
