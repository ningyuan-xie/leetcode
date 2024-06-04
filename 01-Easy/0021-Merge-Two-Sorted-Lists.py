# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Description: Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        # Initiate a new list node to store the merged list
        l3 = ListNode(0)
        # Create a helper list to always point to the beginning of the merged list
        helper_l = l3

        # Case 1: both list has something left
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        # Case 2: l1 has something left
        if l1 is not None:
            l3.next = l1

        # Case 3: l2 has something left
        if l2 is not None:
            l3.next = l2

        # Return the helper list's next node which actually stores the merged list
        return helper_l.next


# Unit Test: Input: l1 = [1,2,4], l2 = [1,3,4], Output: [1,1,2,3,4,4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list3 = Solution.mergeTwoLists(list1, list2)
assert list3.val == 1
assert list3.next.val == 1
assert list3.next.next.val == 2
assert list3.next.next.next.val == 3
assert list3.next.next.next.next.val == 4
assert list3.next.next.next.next.next.val == 4
print("All unit tests are passed")
