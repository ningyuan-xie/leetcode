# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Difficulty: Easy
# Description: Given the root of a binary tree, return the average value of the nodes on each
# level in the form of an array.

from typing import List
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: BFS Traversal. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def averageOfLevels(root: TreeNode) -> List[float]:
        # Initialize the list of average values
        average_values = []
        # Initialize the queue for BFS traversal
        queue = [root]

        # While the queue is not empty
        while queue:
            # Initialize the sum of the node values
            sum_values = 0
            # Initialize the number of nodes
            num_nodes = len(queue)

            # Traverse all the nodes in the current level
            for _ in range(num_nodes):
                # Pop the first node in the queue
                node = queue.pop(0)
                # Add the node value to the sum
                sum_values += node.val

                # Add the left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate the average value of the current level
            average_values.append(sum_values / num_nodes)
        return average_values


# Unit Test: Input: root = [3, 9, 20, None, None, 15, 7], Output: [3.0, 14.5, 11.0]
root_test = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
assert Solution.averageOfLevels(root_test) == [3.0, 14.5, 11.0]

# Unit Test: Input: root = [3, 9, 20, 15, 7], Output: [3.0, 14.5, 11.0]
root_test = TreeNode.build_binary_tree([3, 9, 20, 15, 7])
assert Solution.averageOfLevels(root_test) == [3.0, 14.5, 11.0]

# Unit Test: Input: root = [3, 9, 20, 15, 7, 10, 5], Output: [3.0, 14.5, 9.25]
root_test = TreeNode.build_binary_tree([3, 9, 20, 15, 7, 10, 5])
assert Solution.averageOfLevels(root_test) == [3.0, 14.5, 9.25]

print("All unit tests are passed")
