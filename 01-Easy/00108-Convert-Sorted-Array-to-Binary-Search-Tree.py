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
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n).
        Reverse of 94. Binary Tree Inorder Traversal."""
        # Base Case: If the array is empty, return None
        if not nums:
            return None
        # Recursive Case: Find the middle element and create a node
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        # Recursively build the left and right subtrees
        root.left = Solution.sortedArrayToBST(nums[:mid])
        root.right = Solution.sortedArrayToBST(nums[mid + 1:])
        return root


def unit_tests():
    # Input: nums = [-10,-3,0,5,9], Output: [0,-3,9,-10,null,5]
    root = [-10, -3, 0, 5, 9]
    output = TreeNode.build_binary_tree([0, -3, 9, -10, None, 5])
    assert Solution.sortedArrayToBST(root) == output

    # Input: nums = [1,3], Output: [3,1]
    root = [1, 3]
    output = TreeNode.build_binary_tree([3, 1])
    assert Solution.sortedArrayToBST(root) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
