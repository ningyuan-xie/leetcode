"""203. Remove Linked List Elements
Link: https://leetcode.com/problems/remove-linked-list-elements/
Difficulty: Easy
Description: Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 83. Remove Duplicates from Sorted List."""
        # Create a dummy node to handle edge cases when removing the head node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse the linked list when the current node and the next node are not None
        while current and current.next:
            # If the next node's value is equal to val, skip the next node
            if current.next.val == val:
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return dummy.next


def unit_tests():
    # Input: head = [1,2,6,3,4,5,6], val = 6, Output: [1,2,3,4,5]
    head = ListNode.build_linked_list([1, 2, 6, 3, 4, 5, 6])
    output = ListNode.build_linked_list([1, 2, 3, 4, 5])
    assert Solution.removeElements(head, 6) == output

    # Input: head = [], val = 1, Output: []
    head = ListNode.build_linked_list([])
    output = ListNode.build_linked_list([])
    assert Solution.removeElements(head, 1) == output

    # Input: head = [7,7,7,7], val = 7, Output: []
    head = ListNode.build_linked_list([7, 7, 7, 7])
    output = ListNode.build_linked_list([])
    assert Solution.removeElements(head, 7) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
