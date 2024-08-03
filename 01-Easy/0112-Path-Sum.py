"""112. Path Sum
Link: https://leetcode.com/problems/path-sum/
Difficulty: Easy
Description: Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals targetSum."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1).
           Preorder because we need to process the current node first before left and right subtrees"""
        # Base case: if the tree root is None, return False
        if not root:
            return False
        # 1. Root Case: if the node is a leaf node, check if the sum is equal to the target sum
        if not root.left and not root.right:
            return root.val == targetSum
        # Recursively check if the left or right subtree has a path sum equal to the target sum
        # 2. Recursive Case: Traverse the left subtree
        left_path_sum = Solution.hasPathSum(root.left, targetSum - root.val)
        # 3. Recursive Case: Traverse the right subtree
        right_path_sum = Solution.hasPathSum(root.right, targetSum - root.val)

        # Return True if either the left or right subtree has a path sum equal to the target sum
        return left_path_sum or right_path_sum


# Unit Test: Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22, Output: True
# The tree has a root-to-leaf path 5->4->11->2 which sums up to 22
root_test = TreeNode.build_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
assert Solution.hasPathSum(root_test, 22) == True

# Unit Test: Input: root = [1,2,3], targetSum = 5, Output: False
# The tree has no root-to-leaf path that sums up to 5
root_test = TreeNode.build_binary_tree([1, 2, 3])
assert Solution.hasPathSum(root_test, 5) == False

# Unit Test: Input: root = [1,2], targetSum = 0, Output: False
# The tree has no root-to-leaf path that sums up to 0
root_test = TreeNode.build_binary_tree([1, 2])
assert Solution.hasPathSum(root_test, 0) == False

# Unit Test: Input: root = [], targetSum = 0, Output: False
# The tree is empty
root_test = None
assert Solution.hasPathSum(root_test, 0) == False

print("All unit tests are passed")
