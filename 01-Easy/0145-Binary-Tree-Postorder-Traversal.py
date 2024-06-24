# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Difficulty: Easy
# Description: Given the root of a binary tree, return the postorder traversal of its nodes' values.

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
        # Base case: if the tree root is None, return an empty list
        if not root:
            return []
        # Recursive postorder DFS traversal: left -> right -> root
        else:
            return (Solution.postorderTraversal(root.left) +
                    Solution.postorderTraversal(root.right) +
                    [root.val])


# Unit Test: Input: root = [1,null,2,3], Output: [3,2,1]
assert Solution.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [3, 2, 1]

# Unit Test: Input: root = [], Output: []
assert Solution.postorderTraversal(None) == []

# Unit Test: Input: root = [1], Output: [1]
assert Solution.postorderTraversal(TreeNode(1)) == [1]

print("All unit tests are passed")
