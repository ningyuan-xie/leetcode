# Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Difficulty: Easy
# Description: Given the root of a binary search tree (BST) with duplicates,
# return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# - The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# - Both the left and right subtrees must also be binary search trees.


from typing import List
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Recursive Inorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1)
    # Similar to 0094-Binary-Tree-Inorder-Traversal.py
    # Note: for BST, the inorder traversal will be in ascending order
    @staticmethod
    def findMode(root: TreeNode) -> List[int]:
        modes, current_mode_value, current_mode_frequency, previous_mode_frequency = [], 0, 0, 0

        # Helper function: Inorder DFS Traversal: left -> root -> right
        def inorder_dfs_traversal(node: TreeNode) -> None:
            # nonlocal variables to access the outer scope immutable variables
            nonlocal modes, current_mode_value, current_mode_frequency, previous_mode_frequency
            # Base Case: If the current node is None, do nothing and return
            if not node:
                return
            # Recursive inorder DFS traversal: left -> root -> right
            # 1. Recursive Case: Traverse the left subtree
            inorder_dfs_traversal(node.left)
            # 2. Root Case: Process the current node
            if node.val == current_mode_value:
                current_mode_frequency += 1  # increment the frequency
            else:
                # Update the current mode value and reset the frequency to 1
                current_mode_value, current_mode_frequency = node.val, 1
            # Update the modes list: can return more than one mode
            if current_mode_frequency == previous_mode_frequency:  # pre_mode_freq is the current max
                modes.append(current_mode_value)
            elif current_mode_frequency > previous_mode_frequency:
                # reset the modes list and increase the previous mode frequency
                modes, previous_mode_frequency = [current_mode_value], current_mode_frequency
            # 3. Recursive Case: Traverse the right subtree
            inorder_dfs_traversal(node.right)

        # Start the inorder traversal
        inorder_dfs_traversal(root)
        return modes


# Unit Test: Input: root = [1,null,2,2], Output: [2]
root_test = TreeNode(1, right=TreeNode(2, left=TreeNode(2)))
assert Solution.findMode(root_test) == [2]

# Unit Test: Input: root = [0], Output: [0]
root_test = TreeNode(0)
assert Solution.findMode(root_test) == [0]

# Unit Test: Input: root = [1,1,2], Output: [1]
root_test = TreeNode(1, left=TreeNode(1), right=TreeNode(2))
assert Solution.findMode(root_test) == [1]

print("All unit tests are passed")
