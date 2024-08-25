"""872. Leaf-Similar Trees
Link: https://leetcode.com/problems/leaf-similar-trees/
Difficulty: Easy
Description: Consider all the leaves of a binary tree, from left to right order, the values of those
leaves form a leaf value sequence. Two binary trees are considered leaf-similar if their leaf value
sequence is the same. Return true if and only if the two given trees with head nodes root1 and root2.
"""

from typing import List
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)"""

        def get_leaf_sequence(root: TreeNode) -> List[int]:
            """Helper function to get the leaf value sequence of a binary tree"""
            # Initialize the leaf value sequence
            leaf_sequence = []

            def preorder_dfs_traversal(node: TreeNode) -> None:
                """Helper function to traverse the binary tree in preorder depth-first search"""
                # If the node is a leaf, append the value to the leaf value sequence
                if not node.left and not node.right:
                    leaf_sequence.append(node.val)
                # Otherwise, recursively traverse the left and right children
                else:
                    if node.left:
                        preorder_dfs_traversal(node.left)
                    if node.right:
                        preorder_dfs_traversal(node.right)

            # Start the depth-first search
            preorder_dfs_traversal(root)
            return leaf_sequence

        # Get the leaf value sequence of the two binary trees and compare them
        return get_leaf_sequence(root1) == get_leaf_sequence(root2)


# Unit Test: Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
# root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8], Output: true
root1_test = TreeNode.build_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
root2_test = TreeNode.build_binary_tree(
    [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
assert Solution.leafSimilar(root1_test, root2_test) is True

# Unit Test: Input: root1 = [1], root2 = [1], Output: true
root1_test = TreeNode.build_binary_tree([1])
root2_test = TreeNode.build_binary_tree([1])
assert Solution.leafSimilar(root1_test, root2_test) is True

# Unit Test: Input: root1 = [1], root2 = [2], Output: false
root1_test = TreeNode.build_binary_tree([1])
root2_test = TreeNode.build_binary_tree([2])
assert Solution.leafSimilar(root1_test, root2_test) is False

print("All unit tests are passed")
