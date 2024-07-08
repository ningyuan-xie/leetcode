# Link: https://leetcode.com/problems/binary-tree-paths/
# Difficulty: Easy
# Description: Given the root of a binary tree, return all root-to-leaf paths in any order.

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Recursive DFS. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
        # Base case: if the root is None, return an empty list
        if not root:
            return []

        # Initialize a list to store the root-to-leaf paths
        result = []

        # Helper function to traverse the binary tree and find the root-to-leaf paths
        def dfs_paths(node: TreeNode, path: Optional[str]) -> None:
            # Base case: if the node is a leaf node, append the path to the list of paths
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return

            # Recursive case: traverse the left and right subtrees
            if node.left:
                dfs_paths(node.left, path + str(node.val) + "->")
            if node.right:
                dfs_paths(node.right, path + str(node.val) + "->")

        # Start the DFS traversal from the root node
        dfs_paths(root, "")

        return result


# Unit Test: Input: root = [1,2,3,null,5], Output: ["1->2->5", "1->3"]
root_test = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
assert Solution.binaryTreePaths(root_test) == ["1->2->5", "1->3"]

# Unit Test: Input: root = [1], Output: ["1"]
root_test = TreeNode(1)
assert Solution.binaryTreePaths(root_test) == ["1"]

# Unit Test: Input: root = [1,2], Output: ["1->2"]
root_test = TreeNode(1, TreeNode(2))
assert Solution.binaryTreePaths(root_test) == ["1->2"]

print("All unit tests are passed")
