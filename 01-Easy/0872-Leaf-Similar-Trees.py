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
        """Optimal Solution: Preorder DFS Traversal.
           Time Complexity: O(n), Space Complexity: O(n)"""

        def get_leaf_sequence(node: TreeNode, leaf_sequence: List[int]) -> None:
            """Helper function to get the leaf value sequence of a binary tree using preorder DFS.
               Note that this version returns None instead of List[int],
               unlike 0144-Binary-Tree-Preorder-Traversal.py"""
            # If the node is a leaf, append the value to the leaf value sequence
            if not node.left and not node.right:
                leaf_sequence.append(node.val)
            # Otherwise, recursively traverse the left and right children
            else:
                if node.left:
                    get_leaf_sequence(node.left, leaf_sequence)
                if node.right:
                    get_leaf_sequence(node.right, leaf_sequence)

        # Initialize the leaf sequences for both trees
        leaf_sequence1, leaf_sequence2 = [], []

        # Get the leaf value sequences of the two binary trees
        get_leaf_sequence(root1, leaf_sequence1)
        get_leaf_sequence(root2, leaf_sequence2)

        # Compare the leaf value sequences
        return leaf_sequence1 == leaf_sequence2


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
