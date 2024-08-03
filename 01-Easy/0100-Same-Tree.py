"""100. Same Tree
Link: https://leetcode.com/problems/same-tree/
Difficulty: Easy
Description: Given the roots of two binary trees p and q,
write a function to check if they are the same or not."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1)
           Preorder because we need to compare the roots first before the subtrees"""
        # Base case: if both trees are None, then they are the same
        if not p and not q:
            return True
        # Base case: If one of the trees is None, then they are not the same
        if not p or not q:
            return False
        # 1. Root Case: If the values of the roots are not the same, then they are not the same
        root_same = p.val == q.val
        # 2. Recursive Case: Check if the left subtrees are the same
        left_same = Solution.isSameTree(p.left, q.left)
        # 3. Recursive Case: Check if the right subtrees are the same
        right_same = Solution.isSameTree(p.right, q.right)

        # Return the result of the recursive cases
        return root_same and left_same and right_same


# Unit Test: Input: p = [1,2,3], q = [1,2,3], Output: True
root_test_1 = TreeNode.build_binary_tree([1, 2, 3])
root_test_2 = TreeNode.build_binary_tree([1, 2, 3])
assert Solution.isSameTree(root_test_1, root_test_2) == True

# Unit Test: Input: p = [1,2], q = [1,null,2], Output: False
root_test_1 = TreeNode.build_binary_tree([1, 2])
root_test_2 = TreeNode.build_binary_tree([1, None, 2])
assert Solution.isSameTree(root_test_1, root_test_2) == False

# Unit Test: Input: p = [1,2,1], q = [1,1,2], Output: False
root_test_1 = TreeNode.build_binary_tree([1, 2, 1])
root_test_2 = TreeNode.build_binary_tree([1, 1, 2])
assert Solution.isSameTree(root_test_1, root_test_2) == False

print("All unit tests are passed")
