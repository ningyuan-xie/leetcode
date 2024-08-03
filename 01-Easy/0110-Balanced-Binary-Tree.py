"""110. Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree/
Difficulty: Easy
Description: Given a binary tree, determine if it is height-balanced."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isBalanced(root: Optional[TreeNode]) -> bool:

        def height(node: Optional[TreeNode]) -> int:
            """Helper function: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
               Postorder because we need to traverse the left and right subtrees first before the root.
               Similar to 0104-Maximum-Depth-of-Binary-Tree.py"""
            # Base case: if the node is None, height is -1
            if not node:
                return -1
            # Recursively calculate the height of the left and right subtrees
            # 1. Recursive Case: Traverse the left subtree
            left_height = height(node.left)
            # 2. Recursive Case: Traverse the right subtree
            right_height = height(node.right)
            # 3. Root Case: Return the maximum height of the left and right subtrees
            # + 1 to account for the current node
            return max(left_height, right_height) + 1

        def is_balanced(node: Optional[TreeNode]) -> bool:
            """Helper function: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n).
               Postorder because we need to traverse the left and right subtrees first before the root"""
            # Base case: if the node is None, return True
            if not node:
                return True
            # Recursively check if the left and right subtrees are balanced
            # 1. Recursive Case: Traverse the left subtree
            left_balanced = is_balanced(node.left)
            # 2. Recursive Case: Traverse the right subtree
            right_balanced = is_balanced(node.right)
            # 3. Root Case: Check if the tree is balanced
            # If either subtree is not balanced, return False
            if not left_balanced or not right_balanced:
                return False
            # Check if the difference in height between the left and right subtrees <= 1
            if abs(height(node.left) - height(node.right)) > 1:
                return False
            # If both conditions are met, return True
            return True

        # Call the helper function to check if the tree is balanced
        return is_balanced(root)


# Unit Test: Input: root = [3,9,20,null,null,15,7], Output: True
root_test = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
assert Solution.isBalanced(root_test) == True

# Unit Test: Input: root = [1,2,2,3,3,null,null,4,4], Output: False
root_test = TreeNode.build_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])
assert Solution.isBalanced(root_test) == False

# Unit Test: Input: root = [], Output: True. An empty tree is considered balanced
root_test = TreeNode.build_binary_tree([])
assert Solution.isBalanced(root_test) == True

# Unit Test: Input: root = [1], Output: True. A single node tree is considered balanced
root_test = TreeNode.build_binary_tree([1])
assert Solution.isBalanced(root_test) == True

print("All unit tests are passed")
