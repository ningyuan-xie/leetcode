"""897. Increasing Order Search Tree
Link: https://leetcode.com/problems/increasing-order-search-tree/
Difficulty: Easy
Description: Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child."""

from typing import List, Optional
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def increasingBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Optimal Solution: Inorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""

        def inorder_traversal(node: Optional[TreeNode]) -> List[Optional[TreeNode]]:
            """Helper function to perform in-order traversal on the binary search tree.
            Similar to 94. Binary Tree Inorder Traversal."""
            if not node:
                return []
            return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)

        # Perform in-order traversal on the binary search tree
        nodes = inorder_traversal(root)

        # nodes is now a list of nodes in ascending order with their original children; reconstruct each node (except the last) with no left child and only one right child
        for i in range(len(nodes) - 1):
            nodes[i].left, nodes[i].right = None, nodes[i + 1]

        # The last node in the list should have no left or right child
        nodes[-1].left, nodes[-1].right = None, None

        return nodes[0]


def unit_tests():
    # Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9], Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
    root = TreeNode.build_binary_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
    output = TreeNode.build_binary_tree([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])
    assert Solution.increasingBST(root) == output

    # Input: root = [5,1,7], Output: [1,null,5,null,7]
    root = TreeNode.build_binary_tree([5, 1, 7])
    output = TreeNode.build_binary_tree([1, None, 5, None, 7])
    assert Solution.increasingBST(root) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
