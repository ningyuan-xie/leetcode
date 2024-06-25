# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Difficulty: Easy
# Description: Given the heads of two singly linked-lists headA and headB,
# return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def getIntersectionNode(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if either of the linked lists is empty, return None
        if not headA or not headB:
            return None

        # Initialize two pointers to the heads of the linked lists
        pointerA, pointerB = headA, headB

        # Traverse the linked lists until the two pointers meet at intersection or meet at None
        # Intuition: make the two pointers pass the same total distance, and they will certainly meet
        while pointerA != pointerB:
            # If pointerA reaches the end of the linked list, reset it to the head of the other list
            pointerA = pointerA.next if pointerA else headB
            # If pointerB reaches the end of the linked list, reset it to the head of the other list
            pointerB = pointerB.next if pointerB else headA

        return pointerA


# Unit Test: Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5], Output: ListNode(8)
headA_test = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
headB_test = ListNode(5, ListNode(0, ListNode(1, headA_test.next.next)))
assert Solution.getIntersectionNode(headA_test, headB_test) == headA_test.next.next

# Unit Test: Input: headA = [2,6,4], headB = [1,5], Output: None
headA_test = ListNode(2, ListNode(6, ListNode(4)))
headB_test = ListNode(1, ListNode(5))
assert Solution.getIntersectionNode(headA_test, headB_test) is None

# Unit Test: Input: headA = [1,9,1,2,4], headB = [3,2,4], Output: ListNode(2)
headA_test = ListNode(1, ListNode(9, ListNode(1, ListNode(2, ListNode(4)))))
headB_test = ListNode(3, headA_test.next.next.next)
assert Solution.getIntersectionNode(headA_test, headB_test) == headA_test.next.next.next

print("All unit tests are passed")
