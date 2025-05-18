"""111. Minimum Depth of Binary Tree
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Difficulty: Easy
Description: Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def minDepth(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base Case: If the tree is empty, return 0
        if not root:
            return 0

        # Recursive Case: Calculate the minimum depth of the right subtree
        if not root.left:  # need this otherwise ignore the actual subtree
            return Solution.minDepth(root.right) + 1
        
        # Recursive Case: Calculate the minimum depth of the left subtree
        if not root.right:
            return Solution.minDepth(root.left) + 1

        # Recursive Case: Calculate the minimum depth of both subtrees
        return min(Solution.minDepth(root.left), Solution.minDepth(root.right)) + 1


def unit_tests():
    # Input: root = [3,9,20,null,null,15,7], Output: 2
    root = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert Solution.minDepth(root) == 2

    # Input: root = [2,null,3,null,4,null,5,null,6], Output: 5
    root = TreeNode.build_binary_tree([2, None, 3, None, 4, None, 5, None, 6])
    assert Solution.minDepth(root) == 5

    # Input: root = [1,2], Output: 2
    root = TreeNode.build_binary_tree([1, 2])
    assert Solution.minDepth(root) == 2

    # Input: root = [1,null,2], Output: 2
    root = TreeNode.build_binary_tree([1, None, 2])
    assert Solution.minDepth(root) == 2

    # Input: root = [], Output: 0
    root = TreeNode.build_binary_tree([])
    assert Solution.minDepth(root) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
