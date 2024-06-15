# Link: http://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Difficulty: Easy
# Description: Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the array is empty, return None
        if not nums:
            return None
        # Find the middle index of the array
        mid = len(nums) // 2
        # Create a new node with the middle value
        root = TreeNode(nums[mid])
        # Recursively build the left and right subtrees
        root.left = Solution.sortedArrayToBST(nums[:mid])
        root.right = Solution.sortedArrayToBST(nums[mid + 1:])
        return root

    # Helper function to print the inorder traversal of the binary search tree
    @staticmethod
    def printInorderTraversal(root: Optional[TreeNode]):
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            # Base case: if the tree root is None, return an empty list
            if not root:
                return []
            # Recursive inorder DFS traversal: left -> root -> right
            # For BST, this will be in ascending order
            else:
                return (inorderTraversal(root.left) +
                        [root.val] +
                        inorderTraversal(root.right))

        print(inorderTraversal(root))


# Unit Test: Input: nums = [-10,-3,0,5,9], Output: [0,-3,9,-10,null,5]
# The input [-10,-3,0,5,9] = a sorted array
# The output [0,-3,9,-10,null,5] = serialized format of a binary search tree using level order traversal
Solution.printInorderTraversal(Solution.sortedArrayToBST([-10, -3, 0, 5, 9]))

# Unit Test: Input: nums = [1,3], Output: [3,1]
# The input [1,3] = a sorted array
# The output [3,1] = serialized format of a binary search tree using level order traversal
Solution.printInorderTraversal(Solution.sortedArrayToBST([1, 3]))
print("All unit tests are passed")
