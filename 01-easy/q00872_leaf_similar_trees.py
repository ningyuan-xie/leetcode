"""872. Leaf-Similar Trees
Link: https://leetcode.com/problems/leaf-similar-trees/
Difficulty: Easy
Description: Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""

        def get_leaf_sequence(node: Optional[TreeNode]) -> List[int]:
            """Helper function to get the leaf value sequence of a binary tree using DFS."""
            if not node:
                return []
            
            # If it's a leaf node, return its value
            if not node.left and not node.right:
                return [node.val]
            
            # For internal nodes, combine results from left and right subtrees
            return get_leaf_sequence(node.left) + get_leaf_sequence(node.right)

        # Compare the leaf value sequences
        return get_leaf_sequence(root1) == get_leaf_sequence(root2)
    

def unit_tests(): 
    # Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8], Output: true
    root1 = TreeNode.build_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
    root2 = TreeNode.build_binary_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    assert Solution.leafSimilar(root1, root2) is True

    # Input: root1 = [1], root2 = [1], Output: true
    root1 = TreeNode.build_binary_tree([1])
    root2 = TreeNode.build_binary_tree([1])
    assert Solution.leafSimilar(root1, root2) is True

    # Input: root1 = [1], root2 = [2], Output: false
    root1 = TreeNode.build_binary_tree([1])
    root2 = TreeNode.build_binary_tree([2])
    assert Solution.leafSimilar(root1, root2) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
