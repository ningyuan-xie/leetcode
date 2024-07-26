# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
# Description: Invert a binary tree.

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1)
    # Preorder because we need to process the current node first before the left and right subtrees
    @staticmethod
    def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree root is None, return None
        if not root:
            return None
        # 1. Root Case: Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        # 2. Recursive Case: Invert the left and right subtrees
        Solution.invertTree(root.left)
        # 3. Recursive Case: Invert the right subtree
        Solution.invertTree(root.right)
        return root


# Unit Test: Input: [4, 2, 7, 1, 3, 6, 9]
root_test = TreeNode.build_binary_tree([4, 2, 7, 1, 3, 6, 9])
result = Solution.invertTree(root_test)
print(result)
assert result == TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)),
                          TreeNode(2, TreeNode(3), TreeNode(1)))

# Unit Test: Input: [2, 1, 3]
root_test = TreeNode.build_binary_tree([2, 1, 3])
result = Solution.invertTree(root_test)
print(result)
assert result == TreeNode(2, TreeNode(3), TreeNode(1))

print("All unit tests are passed")
