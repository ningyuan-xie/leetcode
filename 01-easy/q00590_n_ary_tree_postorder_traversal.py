"""590. N-ary Tree Postorder Traversal
Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Difficulty: Easy
Description: Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
Follow up: Recursive solution is trivial, could you do it iteratively?"""

from typing import Optional, List
from package.data_structures import Node


class Solution:
    @staticmethod
    def postorder(root: Optional[Node]) -> List[int]:
        """Optimal Solution: Postorder DFS with a Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        if not root:
            return []
        
        stack = [root]
        result = []
        
        # Iterate until the stack is empty
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push children in normal order to process rightmost child first
            stack.extend(node.children)

        return result[::-1]


def unit_tests():
    # Input: root = [1, None, 3, 2, 4, None, 5, 6], Output: [5, 6, 3, 2, 4, 1]
    root = Node.build_nary_tree([1, None, 3, 2, 4, None, 5, 6])
    assert Solution.postorder(root) == [5, 6, 3, 2, 4, 1]

    # Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14], Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
    root = Node.build_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
    assert Solution.postorder(root) == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]

    # Input: root = [1, None, 2], Output: [2, 1]
    root = Node.build_nary_tree([1, None, 2])
    assert Solution.postorder(root) == [2, 1]

    # Input: root = [], Output: []
    root = Node.build_nary_tree([])
    assert Solution.postorder(root) == []


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
