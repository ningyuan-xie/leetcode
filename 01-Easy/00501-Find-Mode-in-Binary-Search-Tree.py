"""501. Find Mode in Binary Search Tree
Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/
Difficulty: Easy
Description: Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
• The left subtree of a node contains only nodes with keys less than or equal to the node's key.
• The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
• Both the left and right subtrees must also be binary search trees."""

from typing import List
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def findMode(root: TreeNode) -> List[int]:
        """Optimal Solution: Inorder DFS. Time Complexity: O(n), Space Complexity: O(n)."""
        # Dictionary to store the frequency of each value
        count = {}

        def inorder(node: TreeNode) -> None:
            """Helper function to perform inorder traversal and count frequencies. Preorder or postorder traversal can also be used."""
            if not node:
                return
            inorder(node.left)
            count[node.val] = count.get(node.val, 0) + 1
            inorder(node.right)
            
        inorder(root)

        # Find the maximum frequency
        max_count = max(count.values())

        # Return all keys with the maximum frequency
        return [key for key, value in count.items() if value == max_count]


def unit_tests():
    # Input: root = [1,null,2,2], Output: [2]
    root = TreeNode.build_binary_tree([1, None, 2, 2])
    assert Solution.findMode(root) == [2]

    # Input: root = [0], Output: [0]
    root = TreeNode.build_binary_tree([0])
    assert Solution.findMode(root) == [0]

    # Input: root = [1,1,2], Output: [1]
    root = TreeNode.build_binary_tree([1, 1, 2])
    assert Solution.findMode(root) == [1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
