"""700. Search in a Binary Search Tree
Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
Difficulty: Easy
Description: You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null."""

from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def searchBST(root: TreeNode, val: int) -> TreeNode:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(h), Space Complexity: O(h),
           where h is the height of the binary search tree: log(n) <= h <= n."""
        # Base Case: If the root is None or the value is found
        if not root or root.val == val:
            return root
        # Recursive Case: If the value is less than the root's value
        if val < root.val:
            return Solution.searchBST(root.left, val)
        # Recursive Case: If the value is greater than the root's value
        return Solution.searchBST(root.right, val)


# Input: root = [4, 2, 7, 1, 3], val = 2, Output: [2, 1, 3]
root_test = TreeNode.build_binary_tree([4, 2, 7, 1, 3])
root_expected = TreeNode.build_binary_tree([2, 1, 3])
assert Solution.searchBST(root_test, 2) == root_expected

# Input: root = [4, 2, 7, 1, 3], val = 5, Output: None
root_test = TreeNode.build_binary_tree([4, 2, 7, 1, 3])
root_expected = TreeNode.build_binary_tree([])
assert Solution.searchBST(root_test, 5) == root_expected

print("All unit tests are passed.")
