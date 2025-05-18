"""101. Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/
Difficulty: Easy
Description: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""

        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            """Helper function to check if two trees are mirrors of each other."""
            # Base Case: If both nodes are None, return True
            if not left and not right:
                return True
            
            # Base Case: If one node is None and the other is not, return False
            if not left or not right:
                return False
            
            # Recursive Case: Check if the values are equal and the subtrees are mirrors
            return (left.val == right.val
                    and is_mirror(left.left, right.right)
                    and is_mirror(left.right, right.left))

        return is_mirror(root.left, root.right)


def unit_tests():
    # Input: root = [1,2,2,3,4,4,3], Output: True
    root = TreeNode.build_binary_tree([1, 2, 2, 3, 4, 4, 3])
    assert Solution.isSymmetric(root) is True

    # Input: root = [1,2,2,null,3,null,3], Output: False
    root = TreeNode.build_binary_tree([1, 2, 2, None, 3, None, 3])
    assert Solution.isSymmetric(root) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
