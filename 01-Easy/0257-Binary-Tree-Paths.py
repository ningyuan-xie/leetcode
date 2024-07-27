# Link: https://leetcode.com/problems/binary-tree-paths/
# Difficulty: Easy
# Description: Given the root of a binary tree, return all root-to-leaf paths in any order.

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)
    # Similar to 0101-Symmetric-Tree.py, we need an inner helper DFS function to take two parameters
    @staticmethod
    def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
        # Base case: if the root is None, return an empty list
        if not root:
            return []
        # Initialize a list to store the root-to-leaf paths
        result = []
        # don't need to declare it as nonlocal since list is mutable (can change in place),
        # so modifications to the list will be reflected in the outer scope

        # Helper function: Preorder DFS Traversal: root -> left -> right
        # Preorder because we want to append the current node's value to the path first
        def preorder_dfs_path(node: TreeNode, path: Optional[str]) -> None:
            # 1. Root Case: if the node is a leaf node, append the path to the list of paths
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            # Recursive Case: traverse the left and right subtrees
            # and update path along the way using current node's value
            # 2. Recursive Case: Traverse the left subtree
            if node.left:
                preorder_dfs_path(node=node.left, path=path + str(node.val) + "->")
            # 3. Recursive Case: Traverse the right subtree
            if node.right:
                preorder_dfs_path(node=node.right, path=path + str(node.val) + "->")

        # Start the DFS traversal from the root node
        preorder_dfs_path(node=root, path="")
        return result


# Unit Test: Input: root = [1,2,3,null,5], Output: ["1->2->5", "1->3"]
root_test = TreeNode.build_binary_tree([1, 2, 3, None, 5])
assert Solution.binaryTreePaths(root_test) == ["1->2->5", "1->3"]

# Unit Test: Input: root = [1], Output: ["1"]
root_test = TreeNode.build_binary_tree([1])
assert Solution.binaryTreePaths(root_test) == ["1"]

# Unit Test: Input: root = [1,2], Output: ["1->2"]
root_test = TreeNode.build_binary_tree([1, 2])
assert Solution.binaryTreePaths(root_test) == ["1->2"]

print("All unit tests are passed")
