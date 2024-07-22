# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Difficulty: Easy
# Description: Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Inorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)
    # Note: for BST, the inorder traversal will be in ascending order
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        # Base case: if the tree root is None, return an empty list
        if not root:
            return []
        # Recursive inorder DFS traversal: left -> root -> right
        # 1. Recursive Case: Traverse the left subtree
        left_traversal = Solution.inorderTraversal(root.left)
        # 2. Root Case: Process the current node
        root_value = [root.val]
        # 3. Recursive Case: Traverse the right subtree
        right_traversal = Solution.inorderTraversal(root.right)

        return left_traversal + root_value + right_traversal


# Unit Test: Input: root = [1,null,2,3], Output: [1,3,2]
# The input [1,null,2,3] = serialized format of a binary tree using level order traversal,
# where null = a path terminator where no node exists below
assert Solution.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 3, 2]

# Unit Test: Input: root = [], Output: []
assert Solution.inorderTraversal(None) == []

# Unit Test: Input: root = [1], Output: [1]
assert Solution.inorderTraversal(TreeNode(1)) == [1]

print("All unit tests are passed")
