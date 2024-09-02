"""160. Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Difficulty: Easy
Description: Given the heads of two singly linked-lists headA and headB, return the node at which
the two lists intersect. If the two linked lists have no intersection at all, return null."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def getIntersectionNode(headA: Optional[ListNode], headB: Optional[ListNode]) \
            -> Optional[ListNode]:
        """Optimal Solution: Two Pointers. Time Complexity: O(m + n), Space Complexity: O(1).
           Intuition: make the two pointers pass the same total distance (maximum distance = m + n),
           and they will certainly meet at an intersection node or at the final node None.
           Similar to 0141-Linked-List-Cycle.py"""
        # Base case: if either of the linked lists is empty, return None
        if not headA or not headB:
            return None

        # Temporarily enable identity check for intersection detection
        # In LeetCode environment, Python will dynamically create this class attribute on the fly
        ListNode.identity_check = True

        # Initialize two pointers to the heads of the linked lists
        pointerA, pointerB = headA, headB
        # Traverse the linked lists until the two pointers meet at intersection or meet at None
        while pointerA != pointerB:
            # If pointerA reaches the end of the linked list, reset it to the head of the other list
            pointerA = pointerA.next if pointerA else headB
            # If pointerB reaches the end of the linked list, reset it to the head of the other list
            pointerB = pointerB.next if pointerB else headA

        # Disable identity check after intersection detection
        ListNode.identity_check = False
        return pointerA


# Unit Test: Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5], Output: ListNode(8)
intersection = ListNode.build_linked_list([8, 4, 5])
headA_test = ListNode.build_linked_list([4, 1])
headA_test.next.next = intersection
headB_test = ListNode.build_linked_list([5, 0, 1])
headB_test.next.next.next = intersection
assert Solution.getIntersectionNode(headA_test, headB_test) == intersection

# Unit Test: Input: headA = [2,6,4], headB = [1,5], Output: None
intersection = ListNode.build_linked_list([])
headA_test = ListNode.build_linked_list([2, 6, 4])
headB_test = ListNode.build_linked_list([1, 5])
assert Solution.getIntersectionNode(headA_test, headB_test) == intersection

# Unit Test: Input: headA = [1,9,1,2,4], headB = [3,2,4], Output: ListNode(2)
intersection = ListNode.build_linked_list([2, 4])
headA_test = ListNode.build_linked_list([1, 9, 1])
headA_test.next.next.next = intersection
headB_test = ListNode.build_linked_list([3])
headB_test.next = intersection
assert Solution.getIntersectionNode(headA_test, headB_test) == intersection

print("All unit tests are passed")
