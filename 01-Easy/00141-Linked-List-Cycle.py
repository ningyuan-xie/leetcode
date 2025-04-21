"""141. Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy
Description: Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false."""

from package.data_structures import ListNode


class Solution:
    @staticmethod
    def hasCycle(head: ListNode) -> bool:
        """Optimal Solution: Floyd's Cycle Detection Algorithm (Tortoise and Hare). Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize two pointers
        slow = head
        fast = head

        # Enable single value check for cycle detection
        ListNode.identity_check = True

        # Traverse the linked list
        while fast and fast.next:
            # Move slow pointer one step
            slow = slow.next
            # Move fast pointer two steps
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                return True

        # If we reach the end of the list, there is no cycle
        return False


def unit_tests():
    # Input: head = [3,2,0,-4], pos = 1, Output: True
    head = ListNode.build_linked_list([3, 2, 0, -4])
    head.next.next.next.next = head.next  # Connect the tail to the 1st node
    assert Solution.hasCycle(head) is True

    # Input: head = [1,2], pos = 0, Output: True
    head = ListNode.build_linked_list([1, 2])
    head.next.next = head  # Connect the tail to the 0th node
    assert Solution.hasCycle(head) is True

    # Input: head = [1], pos = -1, Output: False
    head = ListNode.build_linked_list([1])
    assert Solution.hasCycle(head) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
