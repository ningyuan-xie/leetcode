"""1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
Difficulty: Medium
Description: Given two binary trees original and cloned and given a reference to a node target in the
original tree.
The cloned tree is a copy of the original tree.
Return a reference to the same node in the cloned tree.
Note that you are not allowed to change any of the two trees or the target node and the answer must
be a reference to a node in the cloned tree."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def getTargetCopy(original: Optional[TreeNode],
                      cloned: Optional[TreeNode],
                      target: Optional[TreeNode]) -> Optional[TreeNode]:
        """Optimal Solution: Preorder DFS. Time Complexity: O(n), Space Complexity: O(n)"""
        # Base case: If the original tree is empty, return None
        if not original:
            return None
        # If the target node is found, return the cloned node (or the original node)
        if original == target:
            return cloned
        # Recursively search the left and right subtree
        return (Solution.getTargetCopy(original.left, cloned.left, target)
                or Solution.getTargetCopy(original.right, cloned.right, target))


# Unit Test: original = [7, 4, 3, None, None, 6, 19], cloned = [7, 4, 3, None, None, 6, 19],
# target = 3, Output: 3
original_test = TreeNode.build_binary_tree([7, 4, 3, None, None, 6, 19])
cloned_test = TreeNode.build_binary_tree([7, 4, 3, None, None, 6, 19])
target_test = original_test.left
assert Solution.getTargetCopy(original_test, cloned_test, target_test) == cloned_test.left

# Unit Test: original = [7], cloned = [7], target = 7, Output: 7
original_test = TreeNode.build_binary_tree([7])
cloned_test = TreeNode.build_binary_tree([7])
target_test = original_test
assert Solution.getTargetCopy(original_test, cloned_test, target_test) == cloned_test

print("All unit tests are passed")
