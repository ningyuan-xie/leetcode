"""257. Binary Tree Paths
Link: https://leetcode.com/problems/binary-tree-paths/
Difficulty: Easy
Description: Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        
        def preorder_dfs(node: Optional[TreeNode], path: str, paths: List[str]) -> None:
            """Helper function to perform DFS and find all root-to-leaf paths."""
            # Base case: if the node is None, return
            if not node:
                return

            # Append the current node's value to the path
            path += str(node.val)

            # If it's a leaf node, add the path to the list of paths
            if not node.left and not node.right:
                paths.append(path)
            else:
                # Continue DFS on left and right children
                path += "->"
                preorder_dfs(node.left, path, paths)
                preorder_dfs(node.right, path, paths)
        
        # Initialize an empty list to store the paths
        paths = []
        # Start DFS from the root node
        preorder_dfs(root, "", paths)
        return paths


def unit_tests():
    # Input: root = [1,2,3,null,5], Output: ["1->2->5", "1->3"]
    root = TreeNode.build_binary_tree([1, 2, 3, None, 5])
    assert Solution.binaryTreePaths(root) == ["1->2->5", "1->3"]

    # Input: root = [1], Output: ["1"]
    root = TreeNode.build_binary_tree([1])
    assert Solution.binaryTreePaths(root) == ["1"]

    # Input: root = [1,2], Output: ["1->2"]
    root = TreeNode.build_binary_tree([1, 2])
    assert Solution.binaryTreePaths(root) == ["1->2"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
