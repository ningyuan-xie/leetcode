"""2331. Evaluate Boolean Binary Tree
Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/
Difficulty: Easy
Description: You are given the root of a full binary tree with the following properties:
- Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
- Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents
the boolean AND.
The evaluation of a node is as follows:
- If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
- Otherwise, evaluate the node's two children and apply the boolean operation of its value with the
children's evaluations.
Return the boolean result of evaluating the root node.
A full binary tree is a binary tree where each node has either 0 or 2 children.
A leaf node is a node that has zero children."""

from typing import Optional
from package.data_structures import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """Optimal Solution: Preorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(n)"""
        # Base Case: Leaf Node's value is 0, return False
        if root.val == 0:
            return False
        # Base Case: Leaf Node's value is 1, return True
        elif root.val == 1:
            return True
        # Recursive Case: Non-Leaf Node's value is 2, return OR of left and right subtree
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # Recursive Case: Non-Leaf Node's value is 3, return AND of left and right subtree
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


# Unit Test: root = [2,1,3,null,null,0,1], Output: true
Solution = Solution()
root_test = TreeNode.build_binary_tree([2, 1, 3, None, None, 0, 1])
assert Solution.evaluateTree(root_test) is True

# Unit Test: root = [0], Output: false
root_test = TreeNode.build_binary_tree([0])
assert Solution.evaluateTree(root_test) is False

print("All unit tests are passed.")
