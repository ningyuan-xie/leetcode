"""203. Remove Linked List Elements
Link: https://leetcode.com/problems/remove-linked-list-elements/
Difficulty: Easy
Description: Remove all elements from a linked list of integers that have value val."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)
           Similar to 0083-Remove-Duplicates-from-Sorted-List.py"""
        # Initialize a dummy node to avoid edge cases
        dummy = ListNode(0)
        dummy.next = head
        # Initialize the current node as the dummy node
        current = dummy
        # Iterate through the linked list
        while current.next:
            # If the next node has the target value, skip the next node
            if current.next.val == val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        return dummy.next  # dummy: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None


# Unit Test: Input: head = [1,2,6,3,4,5,6], val = 6, Output: [1,2,3,4,5]
head_test = ListNode.build_linked_list([1, 2, 6, 3, 4, 5, 6])
head_expected = ListNode.build_linked_list([1, 2, 3, 4, 5])
assert Solution.removeElements(head_test, 6) == head_expected

# Unit Test: Input: head = [], val = 1, Output: []
head_test = ListNode.build_linked_list([])
head_expected = ListNode.build_linked_list([])
assert Solution.removeElements(head_test, 1) == head_expected

# Unit Test: Input: head = [7,7,7,7], val = 7, Output: []
head_test = ListNode.build_linked_list([7, 7, 7, 7])
head_expected = ListNode.build_linked_list([])
assert Solution.removeElements(head_test, 7) == head_expected

print("All unit tests are passed")
