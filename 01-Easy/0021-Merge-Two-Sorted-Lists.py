"""21. Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Description: Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists."""

from package.data_structures import ListNode


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        """Optimal Solution: Iteration. Time Complexity: O(n + m), Space Complexity: O(1)"""
        # Dummy node to keep track of the head of the linked list
        dummy = ListNode()  # dummy: 0 -> None
        # Tail node to keep track of the last node of the linked list
        tail = dummy  # tail: 0 -> None
        # both dummy and tail refer to the same mutable object

        # Traverse both linked lists until one of them is empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next  # append the whole l1, not just a value
            else:
                tail.next, l2 = l2, l2.next  # append the whole l2, not just a value
            # Move the tail to the next node after appending
            tail = tail.next

        # Append the remaining nodes of l1 or l2
        tail.next = l1 or l2
        # return dummy.next to exclude the head node
        return dummy.next  # dummy: 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None


# Unit Test: Input: l1 = [1,2,4], l2 = [1,3,4], Output: [1,1,2,3,4,4]
list1 = ListNode.build_linked_list([1, 2, 4])
list2 = ListNode.build_linked_list([1, 3, 4])
list_expected = ListNode.build_linked_list([1, 1, 2, 3, 4, 4])
assert Solution.mergeTwoLists(list1, list2) == list_expected

print("All unit tests are passed")
