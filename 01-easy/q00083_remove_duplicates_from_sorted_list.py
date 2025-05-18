"""83. Remove Duplicates from Sorted List
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Difficulty: Easy
Description: Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        current = head

        # Traverse the linked list when the current node and the next node are not None
        while current and current.next:
            # If the current node's value is equal to the next node's value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head


def unit_tests():
    # Input: head = [1,1,2], Output: [1,2]
    head = ListNode.build_linked_list([1, 1, 2])
    output = ListNode.build_linked_list([1, 2])
    assert Solution.deleteDuplicates(head) == output

    # Input: head = [1,1,2,3,3], Output: [1,2,3]
    head = ListNode.build_linked_list([1, 1, 2, 3, 3])
    output = ListNode.build_linked_list([1, 2, 3])
    assert Solution.deleteDuplicates(head) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
