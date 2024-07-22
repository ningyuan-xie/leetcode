# Link: https://leetcode.com/problems/same-tree/
# Difficulty: Easy
# Description: Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1)
    # Preorder because we need to compare the roots first before the subtrees
    @staticmethod
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both trees are None, then they are the same
        if not p and not q:
            return True
        # Base case: If one of the trees is None, then they are not the same
        if not p or not q:
            return False
        # 1. Root Case: If the values of the roots are not the same, then they are not the same
        if p.val != q.val:
            return False
        # 2. Recursive Case: Check if the left subtrees are the same
        left_same = Solution.isSameTree(p.left, q.left)
        # 3. Recursive Case: Check if the right subtrees are the same
        right_same = Solution.isSameTree(p.right, q.right)

        # Return the result of the recursive cases
        return left_same and right_same


# Unit Test: Input: p = [1,2,3], q = [1,2,3], Output: True
# The input [1,2,3] = serialized format of a binary tree using level order traversal
assert Solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)),
                           TreeNode(1, TreeNode(2), TreeNode(3))) == True

# Unit Test: Input: p = [1,2], q = [1,null,2], Output: False
# The input [1,2] = serialized format of a binary tree using level order traversal
assert Solution.isSameTree(TreeNode(1, TreeNode(2)),
                           TreeNode(1, None, TreeNode(2))) == False

# Unit Test: Input: p = [1,2,1], q = [1,1,2], Output: False
# The input [1,2,1] = serialized format of a binary tree using level order traversal
assert Solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)),
                           TreeNode(1, TreeNode(1), TreeNode(2))) == False

print("All unit tests are passed")
