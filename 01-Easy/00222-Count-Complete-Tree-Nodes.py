"""222. Count Complete Tree Nodes
Link: https://leetcode.com/problems/count-complete-tree-nodes/
Difficulty: Easy
Description: Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def countNodes(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log^2(n)), Space Complexity: O(1)."""
        # Base Case: If the tree is empty, return 0
        if not root:
            return 0
        
        def getHeight(node: Optional[TreeNode], goLeft: bool) -> int:
            """Helper function to calculate the height of the tree. Time Complexity: O(log(n))."""
            height = -1
            while node:
                node = node.left if goLeft else node.right
                height += 1
            return height

        left_height = getHeight(root, True)
        right_height = getHeight(root, False)

        if left_height == right_height:
            # Tree is perfect: 2^(h+1) - 1 nodes
            return 2**(left_height + 1) - 1
        else:
            # Not perfect, recurse on left and right
            return Solution.countNodes(root.left) + Solution.countNodes(root.right) + 1


def unit_tests():
    # Input: root = [1,2,3,4,5,6], Output: 6
    root = TreeNode.build_binary_tree([1, 2, 3, 4, 5, 6])
    assert Solution.countNodes(root) == 6

    # Input: root = [1,2,3,4,5,6,7], Output: 7
    root = TreeNode.build_binary_tree([1, 2, 3, 4, 5, 6, 7])
    assert Solution.countNodes(root) == 7

    # Input: root = [], Output: 0
    root = TreeNode.build_binary_tree([])
    assert Solution.countNodes(root) == 0

    # Input: root = [1], Output: 1
    root = TreeNode.build_binary_tree([1])
    assert Solution.countNodes(root) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
