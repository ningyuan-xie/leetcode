"""653. Two Sum IV - Input is a BST
Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Difficulty: Easy
Description: Given the root of a Binary Search Tree and a target number k, return true if
there exist two elements in the BST such that their sum is equal to the given target."""

from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def findTarget(root: TreeNode, k: int) -> bool:
        """Optimal Solution: Inorder DFS & Two Pointers.
           Time Complexity: O(n), Space Complexity: O(n)"""

        def inorder(node: TreeNode) -> list[int]:
            """Helper function: same as 0094-Binary-Tree-Inorder-Traversal.py"""
            if node is None:
                return []
            # Traverse the left subtree, visit the node, then traverse the right subtree
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Get the sorted elements of the BST via in-order traversal
        sorted_elements = inorder(root)

        # Initialize two pointers for the two-pointer technique
        left, right = 0, len(sorted_elements) - 1
        while left < right:
            # Calculate the sum of the elements at the two pointers
            current_sum = sorted_elements[left] + sorted_elements[right]
            if current_sum == k:
                return True  # Found two numbers that add up to k
            elif current_sum < k:
                left += 1  # Increase the sum by moving the left pointer to the right
            else:
                right -= 1  # Decrease the sum by moving the right pointer to the left
        return False  # No pair found that adds up to k


# Input: root = [5, 3, 6, 2, 4, None, 7], k = 9, Output: True
root_test = TreeNode.build_binary_tree([5, 3, 6, 2, 4, None, 7])
assert Solution.findTarget(root_test, 9) is True

# Input: root = [5, 3, 6, 2, 4, None, 7], k = 28, Output: False
root_test = TreeNode.build_binary_tree([5, 3, 6, 2, 4, None, 7])
assert Solution.findTarget(root_test, 28) is False

# Input: root = [2, 1, 3], k = 4, Output: True
root_test = TreeNode.build_binary_tree([2, 1, 3])
assert Solution.findTarget(root_test, 4) is True

print("All unit tests are passed.")
