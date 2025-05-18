"""21. Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Description: You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Optimal Solution: Iterative Merge. Time Complexity: O(n + m), Space Complexity: O(1)."""
        dummy = ListNode(0)  # Dummy head for the merged list
        current = dummy

        # Traverse both lists and append the smaller node to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the current pointer to the next node
            current = current.next

        # Append any remaining nodes from either list
        current.next = list1 if list1 else list2
        return dummy.next


def unit_tests():
    # Input: list1 = [1,2,4], list2 = [1,3,4], Output: [1,1,2,3,4,4]
    list1 = ListNode.build_linked_list([1, 2, 4])
    list2 = ListNode.build_linked_list([1, 3, 4])
    output = ListNode.build_linked_list([1, 1, 2, 3, 4, 4])
    assert Solution.mergeTwoLists(list1, list2) == output

    # Input: list1 = [], list2 = [], Output: []
    list1 = ListNode.build_linked_list([])
    list2 = ListNode.build_linked_list([])
    output = ListNode.build_linked_list([])
    assert Solution.mergeTwoLists(list1, list2) == output

    # Input: list1 = [], list2 = [0], Output: [0]
    list1 = ListNode.build_linked_list([])
    list2 = ListNode.build_linked_list([0])
    output = ListNode.build_linked_list([0])
    assert Solution.mergeTwoLists(list1, list2) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
