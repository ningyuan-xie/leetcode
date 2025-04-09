"""108. Convert Sorted Array to Binary Search Tree
Link: http://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Difficulty: Easy
Description: Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n).
           Preorder because we want to process the current node first.
           Reverse of 0094-Binary-Tree-Inorder-Traversal.py"""
        # Base case: if the array is empty, return None
        if not nums:
            return None
        # 1. Root Case: Find the middle index of the array
        mid = len(nums) // 2  # E.g. [-10,-3,0,5,9] -> mid = 2
        # Create a new node with the middle value
        root = TreeNode(nums[mid])  # E.g. [-10,-3,0,5,9] -> mid = 2, root = 0
        # Recursively build the left and right subtrees
        # 2. Recursive Case: Traverse the left subtree
        root.left = Solution.sortedArrayToBST(nums[:mid])  # E.g. [-10,-3] -> mid = 1, root = -3
        # 3. Recursive Case: Traverse the right subtree
        root.right = Solution.sortedArrayToBST(nums[mid + 1:])  # E.g. [5,9] -> mid = 1, root = 9
        # Note: for root.right, [-10][1] will return an error, but [-10][1:] will actually return []
        return root
        # Actual return: TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
        # Level order traversal list format: [0,-3,9,-10,null,5]


# Input: nums = [-10,-3,0,5,9], Output: [0,-3,9,-10,null,5]
root_test = [-10, -3, 0, 5, 9]
root_expected = TreeNode.build_binary_tree([0, -3, 9, -10, None, 5])
assert Solution.sortedArrayToBST(root_test) == root_expected

# Input: nums = [1,3], Output: [3,1]
root_test = [1, 3]
root_expected = TreeNode.build_binary_tree([3, 1])
assert Solution.sortedArrayToBST(root_test) == root_expected

print("All unit tests are passed.")
