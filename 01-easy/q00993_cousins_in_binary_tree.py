"""993. Cousins in Binary Tree
Link: https://leetcode.com/problems/cousins-in-binary-tree/
Difficulty: Easy
Description: Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isCousins(root: Optional[TreeNode], x: int, y: int) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Variables to store the depth and parent of x and y
        x_info, y_info = [-1, None], [-1, None]  # [depth, parent]

        def preorder_dfs_depth_parent(node: Optional[TreeNode], depth: int = 0, parent: Optional[TreeNode] = None) -> None:
            """Helper function to traverse the tree in preorder DFS."""
            if not node:
                return

            # If we find x, store its depth and parent
            if node.val == x:
                x_info[0], x_info[1] = depth, parent

            # If we find y, store its depth and parent
            if node.val == y:
                y_info[0], y_info[1] = depth, parent

            # Traverse the left and right subtrees with updated depth and parent
            preorder_dfs_depth_parent(node.left, depth + 1, node)
            preorder_dfs_depth_parent(node.right, depth + 1, node)

        # Start DFS from the root (depth 0, no parent)
        preorder_dfs_depth_parent(root, 0, None)

        # Nodes are cousins if they have the same depth but different parents
        return x_info[0] == y_info[0] and x_info[1] != y_info[1]


def unit_tests():
    # Input: [1,2,3,4], x = 4, y = 3, Output: False
    root = TreeNode.build_binary_tree([1, 2, 3, 4])
    assert Solution.isCousins(root, 4, 3) is False

    # Input: [1,2,3,None,4,None,5], x = 5, y = 4, Output: True
    root = TreeNode.build_binary_tree([1, 2, 3, None, 4, None, 5])
    assert Solution.isCousins(root, 5, 4) is True

    # Input: [1,2,3,None,4], x = 2, y = 3, Output: False
    root = TreeNode.build_binary_tree([1, 2, 3, None, 4])
    assert Solution.isCousins(root, 2, 3) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
