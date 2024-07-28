# Link: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Difficulty: Easy
# Description: Given a n-ary tree, find its maximum depth.

from typing import Optional
from package.data_structures import Node


class Solution:
    # Optimal Solution: Postorder DFS Traversal. Time Complexity: O(n), Space Complexity: O(1)
    # Similar to 0104-Maximum-Depth-of-Binary-Tree.py and 0543-Diameter-of-Binary-Tree.py
    @staticmethod
    def maxDepth(root: Optional[Node]) -> int:
        # Base Case: If the current node is None, return 0
        if not root:
            return 0
        # Base Case: If the current node is a leaf node (no children), return 1 and go back up
        # This base case is necessary since max() cannot take an empty list
        if not root.children:
            return 1
        # Initialize a list to store the depths of all children
        child_depths = []
        # Iterate over each child first before the root
        for child in root.children:
            # Access order: [1, 3, 5, 6, 2, 4] -- the same as preorder traversal
            # Actual depth calculation order: [5, 6, 3, 2, 4, 1] -- the actual postorder traversal
            # 1. Recursive Case: Traverse each child and store their depths
            child_depths.append(Solution.maxDepth(child))  # 3: [1, 1] and return 2; 1: [2, 1, 1]
        # 2. Root Case: After traversing all children, find the maximum depth among them,
        # and +1 to account for the current node
        return max(child_depths) + 1


# Unit Test: Input: root = [1, None, 3, 2, 4, None, 5, 6], Output: 3
root_test = Node.build_nary_tree([1, None, 3, 2, 4, None, 5, 6])
print(root_test)
assert Solution.maxDepth(root_test) == 3

# Unit Test: Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
# None, None, 11, None, 12, None, 13, None, None, 14], Output: 5
root_test = Node.build_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
                                  None, None, 11, None, 12, None, 13, None, None, 14])
print(root_test)
assert Solution.maxDepth(root_test) == 5

# Unit Test: Input: root = [1, None, 2], Output: 2
root_test = Node.build_nary_tree([1, None, 2])
print(root_test)
assert Solution.maxDepth(root_test) == 2

# Unit Test: Input: root = [], Output: 0
root_test = Node.build_nary_tree([])
assert Solution.maxDepth(root_test) == 0

print("All unit tests are passed")
