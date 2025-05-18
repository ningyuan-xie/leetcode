"""206. Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Description: Given the head of a singly linked list, reverse the list, and return the reversed list."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        """Optimal Solution: Three Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize previous and current pointers
        new_list = None  # always points to the head of the new list
        current = head  # used to traverse the original list

        while current:
            # Store the next node
            next_node = current.next
            # Reverse the link
            current.next = new_list
            # Move the pointers one position forward
            new_list = current
            current = next_node

        return new_list


def unit_tests():
    # Input: head = [1,2,3,4,5], Output: [5,4,3,2,1]
    head = ListNode.build_linked_list([1, 2, 3, 4, 5])
    output = ListNode.build_linked_list([5, 4, 3, 2, 1])
    assert Solution.reverseList(head) == output

    # Input: head = [1,2], Output: [2,1]
    head = ListNode.build_linked_list([1, 2])
    output = ListNode.build_linked_list([2, 1])
    assert Solution.reverseList(head) == output

    # Input: head = [], Output: []
    head = ListNode.build_linked_list([])
    output = ListNode.build_linked_list([])
    assert Solution.reverseList(head) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
