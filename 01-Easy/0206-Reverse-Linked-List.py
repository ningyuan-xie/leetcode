# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Description: Reverse a singly linked list.

from typing import Optional
from package.data_structures import ListNode


class Solution:
    # Optimal Solution: Iterative. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers to store the previous and current nodes
        prev, current = None, head
        # Iterate through the linked list
        while current:  # [1, 2, 3] -> [2, 3] -> [3]
            # Save the next node for the next iteration
            next_node = current.next  # [2, 3] -> [3] -> None
            # Break the current's next node and point to the previous node
            current.next = prev  # current: [1] -> [2, 1] -> [3, 2, 1]
            # Move to the next node by updating two pointers; prev is now the new head
            prev, current = current, next_node
            # prev: [1] -> [2, 1] -> [3, 2, 1]; current: [2, 3] -> [3] -> None
        return prev
        # [1 -> 2 -> 3 -> None] becomes [None <- 1 <- 2 <- 3]


# Unit Test: Input: head = [1,2,3,4,5], Output: [5,4,3,2,1]
head_test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = Solution.reverseList(head_test)
print(result)
assert result == ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))

# Unit Test: Input: head = [1,2], Output: [2,1]
head_test = ListNode(1, ListNode(2))
result = Solution.reverseList(head_test)
print(result)
assert result == ListNode(2, ListNode(1))

# Unit Test: Input: head = [], Output: []
head_test = None
result = Solution.reverseList(head_test)
assert result is None

print("All unit tests are passed")
