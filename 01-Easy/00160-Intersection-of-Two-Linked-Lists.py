"""160. Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Difficulty: Easy
Description: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize two pointers
        pointerA = headA
        pointerB = headB

        # Enable single value check for cycle detection
        ListNode.identity_check = True

        # Traverse both lists
        while pointerA != pointerB:
            # Move to the next node or switch to the other list
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # Return the intersection node or None if no intersection
        return pointerA


def unit_tests():
    # Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3, Output: Intersected at '8'
    intersection = ListNode.build_linked_list([8, 4, 5])
    listA = ListNode.build_linked_list([4, 1])
    listA.next.next = intersection
    listB = ListNode.build_linked_list([5, 0, 1])
    listB.next.next.next = intersection
    assert Solution.getIntersectionNode(listA, listB) == intersection

    # Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1, Output: Intersected at '2'
    intersection = ListNode.build_linked_list([2, 4])
    listA = ListNode.build_linked_list([1, 9, 1])
    listA.next.next.next = intersection
    listB = ListNode.build_linked_list([3])
    listB.next = intersection
    assert Solution.getIntersectionNode(listA, listB) == intersection

    # Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2, Output: No intersection
    intersection = ListNode.build_linked_list([])
    listA = ListNode.build_linked_list([2, 6, 4])
    listB = ListNode.build_linked_list([1, 5])
    assert Solution.getIntersectionNode(listA, listB) == intersection


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
