# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Difficulty: Easy
# Description: Given the root of a binary tree, return the preorder traversal of its nodes' values.

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Recursive DFS. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
        # Base case: if the tree root is None, return an empty list
        if not root:
            return []
        # Recursive preorder DFS traversal: root -> left -> right
        else:
            return ([root.val] +
                    Solution.preorderTraversal(root.left) +
                    Solution.preorderTraversal(root.right))


# Unit Test: Input: root = [1,null,2,3], Output: [1,2,3]
assert Solution.preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 2, 3]

# Unit Test: Input: root = [], Output: []
assert Solution.preorderTraversal(None) == []

# Unit Test: Input: root = [1], Output: [1]
assert Solution.preorderTraversal(TreeNode(1)) == [1]

print("All unit tests are passed")
