"""111. Minimum Depth of Binary Tree
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Difficulty: Easy
Description: Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def minDepth(root: Optional[TreeNode]) -> int:
        """Optimal Solution: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Postorder because we need to traverse the left and right subtrees first before the root.
           Similar to 0104-Maximum-Depth-of-Binary-Tree.py"""
        # Base case: if the tree root is None, return 0
        if not root:
            return 0
        # Postorder DFS Traversal: return the minimum depth of the left and right subtrees
        # 1. Recursive Case: Traverse the left subtree
        left_depth = Solution.minDepth(root.left)
        # 2. Recursive Case: Traverse the right subtree
        right_depth = Solution.minDepth(root.right)
        # 3. Root Case:
        # If either the left or right subtree is empty, return the non-empty subtree + 1
        # + 1 to account for the current node
        if not root.left or not root.right:
            return left_depth + right_depth + 1
        # Return the minimum depth of the left and right subtrees
        # + 1 to account for the current node
        return min(left_depth, right_depth) + 1


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: 2
root_test = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
assert Solution.minDepth(root_test) == 2

# Unit Test: Input: root = [2,null,3,null,4,null,5,null,6], Output: 5
root_test = TreeNode.build_binary_tree([2, None, 3, None, 4, None, 5, None, 6])
assert Solution.minDepth(root_test) == 5

# Unit Test: Input: root = [1,2], Output: 2
root_test = TreeNode.build_binary_tree([1, 2])
assert Solution.minDepth(root_test) == 2

# Unit Test: Input: root = [1,null,2], Output: 2
root_test = TreeNode.build_binary_tree([1, None, 2])
assert Solution.minDepth(root_test) == 2

# Unit Test: Input: root = [], Output: 0
root_test = TreeNode.build_binary_tree([])
assert Solution.minDepth(root_test) == 0

print("All unit tests are passed")
