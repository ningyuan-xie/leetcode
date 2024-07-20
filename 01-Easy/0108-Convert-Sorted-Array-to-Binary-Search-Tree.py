# Link: http://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Difficulty: Easy
# Description: Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Recursive DFS. Time Complexity: O(n), Space Complexity: O(n)
    # Reverse of 0094-Binary-Tree-Inorder-Traversal.py
    @staticmethod
    def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the array is empty, return None
        if not nums:
            return None
        # Find the middle index of the array
        mid = len(nums) // 2  # E.g. [-10,-3,0,5,9] -> mid = 2
        # Create a new node with the middle value
        root = TreeNode(nums[mid])  # E.g. [-10,-3,0,5,9] -> mid = 2, root = 0
        # Recursively build the left and right subtrees
        root.left = Solution.sortedArrayToBST(nums[:mid])  # E.g. [-10,-3] -> mid = 1, root = -3
        root.right = Solution.sortedArrayToBST(nums[mid + 1:])  # E.g. [5,9] -> mid = 1, root = 9
        # Note: for root.right, [-10][1] will return an error, but [-10][1:] will actually return []
        return root
        # Actual return: TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
        # Level order traversal list format: [0,-3,9,-10,null,5]

    # 0094-Binary-Tree-Inorder-Traversal.py
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


# Unit Test: Input: nums = [-10,-3,0,5,9], Output: [0,-3,9,-10,null,5]
# The input [-10,-3,0,5,9] = a sorted array
# Output: TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
# Output (Level order traversal list format): [0,-3,9,-10,null,5]
# Output (Inorder traversal list format): [-10,-3,0,5,9]
nums_test = [-10, -3, 0, 5, 9]
result = Solution.sortedArrayToBST(nums_test)
print(result)
assert Solution.inorderTraversal(result) == [-10, -3, 0, 5, 9]

# Unit Test: Input: nums = [1,3], Output: [3,1]
# The input [1,3] = a sorted array
# Output: TreeNode(3, TreeNode(1))
# Output (Level order traversal list format): [3,1]
# Output (Inorder traversal list format): [1,3]
nums_test = [1, 3]
result = Solution.sortedArrayToBST(nums_test)
print(result)
assert Solution.inorderTraversal(result) == [1, 3]

print("All unit tests are passed")
