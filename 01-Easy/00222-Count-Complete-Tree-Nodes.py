"""222. Count Complete Tree Nodes
Link: https://leetcode.com/problems/count-complete-tree-nodes/
Difficulty: Easy
Description: Given the root of a complete binary tree, return the number of the nodes in the tree."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def countNodes(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Postorder because we need to traverse the left and right subtrees first before the root.
           Similar to 0104-Maximum-Depth-of-Binary-Tree.py"""
        # Base case: if the root is None, return 0
        if not root:
            return 0
        # 1. Recursive Case: Traverse the left subtree
        left_count = Solution.countNodes(root.left)
        # 2. Recursive Case: Traverse the right subtree
        right_count = Solution.countNodes(root.right)
        # 3. Root Case: Return the total number of nodes in the left and right subtrees
        # + 1 for the current node
        root_count = left_count + right_count + 1

        return root_count


# Unit Test: Input: [1,2,3,4,5,6], Output: 6
root_test = TreeNode.build_binary_tree([1, 2, 3, 4, 5, 6])
assert Solution.countNodes(root_test) == 6

# Unit Test: Input: [1,2,3,4,5,6,7], Output: 7
root_test = TreeNode.build_binary_tree([1, 2, 3, 4, 5, 6, 7])
assert Solution.countNodes(root_test) == 7

print("All unit tests are passed")
