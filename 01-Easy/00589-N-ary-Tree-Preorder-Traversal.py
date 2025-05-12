"""589. N-ary Tree Preorder Traversal
Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Difficulty: Easy
Description: Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples).
Follow up: Recursive solution is trivial, could you do it iteratively?"""

from typing import Optional, List
from package.data_structures import Node


class Solution:
    @staticmethod
    def preorder(root: Optional[Node]) -> List[int]:
        """Optimal Solution: Preorder DFS with a Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        if not root:
            return []
        
        stack = [root]
        result = []
        
        # Iterate until the stack is empty
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push children in reverse order to process leftmost child next
            stack.extend(reversed(node.children))
        
        return result


def unit_tests():
    # Input: root = [1, None, 3, 2, 4, None, 5, 6], Output: [1, 3, 5, 6, 2, 4]
    root = Node.build_nary_tree([1, None, 3, 2, 4, None, 5, 6])
    assert Solution.preorder(root) == [1, 3, 5, 6, 2, 4]

    # Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14], Output: [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
    root = Node.build_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
    assert Solution.preorder(root) == [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

    # Input: root = [1, None, 2], Output: [1, 2]
    root = Node.build_nary_tree([1, None, 2])
    assert Solution.preorder(root) == [1, 2]

    # Input: root = [], Output: []
    root = Node.build_nary_tree([])
    assert Solution.preorder(root) == []


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
