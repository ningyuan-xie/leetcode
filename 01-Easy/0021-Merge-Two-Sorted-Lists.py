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
        # Dummy node to keep track of the head of the linked list
        dummy = ListNode() # dummy: 0 -> None
        # Tail node to keep track of the last node of the linked list
        tail = dummy # tail: 0 -> None
        # both dummy and tail refer to the same mutable object

        # Traverse both linked lists until one of them is empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 # append the whole l1, not just a value
                l1 = l1.next
            else:
                tail.next = l2 # append the whole l2, not just a value
                l2 = l2.next
            # Move the tail to the next node after appending
            tail = tail.next

        # Append the remaining nodes of l1 or l2
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        # return dummy.next to exclude the head node
        return dummy.next # dummy: 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

    # Helper function to print the linked list
    def printLinkedList(l: ListNode):
        while l:
            print(l.val, end=" -> ")
            l = l.next
        print("None")

# Unit Test: Input: l1 = [1,2,4], l2 = [1,3,4], Output: [1,1,2,3,4,4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = Solution.mergeTwoLists(list1, list2)
Solution.printLinkedList(list3)
print("All unit tests are passed")
