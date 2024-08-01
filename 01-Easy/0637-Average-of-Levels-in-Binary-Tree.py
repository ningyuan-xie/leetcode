# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Difficulty: Easy
# Description: Given the root of a binary tree, return the average value of the nodes on each
# level in the form of an array.

from typing import List
from package.data_structures import TreeNode


class Solution:
    # Optimal Solution: BFS Traversal. Time Complexity: O(n), Space Complexity: O(n)
    # Similar to the reverse of TreeNode.build_binary_tree() method
    # E.g. [3, 9, 20, None, None, 15, 7] -> pop 3, append 9, 20 -> pop 9 -> pop 20, append 15, 7
    @staticmethod
    def averageOfLevels(root: TreeNode) -> List[float]:
        # Initialize the output list, and the queue for BFS traversal
        average_values = []
        queue = [root]

        # While the queue is not empty
        while queue:
            # Initialize the sum of the node values, and the number of nodes in the current level
            sum_values = 0
            current_level_num_nodes = len(queue)

            # Traverse all the nodes in the current level
            for _ in range(current_level_num_nodes):
                # Pop the first node in the queue
                current = queue.pop(0)  # FIFO: 1st element is the new parent
                # Add the node value to the sum
                sum_values += current.val

                # Add the left and right children to the queue
                if current.left:
                    queue.append(current.left)  # Append the left subtree
                if current.right:
                    queue.append(current.right)  # Append the right subtree

            # Calculate the average value of the current level
            average_values.append(sum_values / current_level_num_nodes)
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
