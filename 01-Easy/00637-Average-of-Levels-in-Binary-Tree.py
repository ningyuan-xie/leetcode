"""637. Average of Levels in Binary Tree
Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
Difficulty: Easy
Description: Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted."""

from typing import List
from package.data_structures import TreeNode


class Solution:
    @staticmethod
    def averageOfLevels(root: TreeNode) -> List[float]:
        """Optimal Solution: BFS. Time Complexity: O(n), Space Complexity: O(n)."""
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
                # FIFO: 1st element is the new parent
                current = queue.pop(0)
                sum_values += current.val

                # Add the left and right children to the queue
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            # Calculate the average value of the current level
            average_values.append(sum_values / current_level_num_nodes)
            
        return average_values


def unit_test():
    # Input: root = [3, 9, 20, None, None, 15, 7], Output: [3.0, 14.5, 11.0]
    root = TreeNode.build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert Solution.averageOfLevels(root) == [3.0, 14.5, 11.0]

    # Input: root = [3, 9, 20, 15, 7], Output: [3.0, 14.5, 11.0]
    root = TreeNode.build_binary_tree([3, 9, 20, 15, 7])
    assert Solution.averageOfLevels(root) == [3.0, 14.5, 11.0]

    # Input: root = [3, 9, 20, 15, 7, 10, 5], Output: [3.0, 14.5, 9.25]
    root = TreeNode.build_binary_tree([3, 9, 20, 15, 7, 10, 5])
    assert Solution.averageOfLevels(root) == [3.0, 14.5, 9.25]


if __name__ == "__main__":
    unit_test()
    print("All unit tests are passed.")
