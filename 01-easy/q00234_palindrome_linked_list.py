"""234. Palindrome Linked List
Link: https://leetcode.com/problems/palindrome-linked-list/
Difficulty: Easy
Description: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
Follow up: Could you do it in O(n) time and O(1) space?"""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def isPalindrome(head: Optional[ListNode]) -> bool:
        """Optimal Solution: Reverse Half. Time Complexity: O(n), Space Complexity: O(1)."""

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            """Helper function to reverse a linked list: from 206. Reverse Linked List."""
            # Initialize previous and current pointers
            new_list = None  # always points to the head of the new list
            current = head  # used to traverse the original list

            while current:
                # Store the next node
                next_node = current.next
                # Reverse the link
                current.next = new_list
                # Move the pointers one position forward
                new_list = current
                current = next_node

            return new_list

        # Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:  # E.g. [1, 2, 3, 2, 1]
            slow, fast = slow.next, fast.next.next  # slow stops at 3, fast stops at 1

        # Reverse the second half of the linked list
        second_half = reverseList(slow)  # [3, 2, 1] -> [1, 2, 3]

        # Compare the first half and the second half of the linked list
        first_half = head
        while second_half:  # Compare [1, 2, 3, 2, 1] and [1, 2, 3]
            if first_half.val != second_half.val:
                return False
            first_half, second_half = first_half.next, second_half.next
        return True


def unit_tests():
    # Input: head = [1, 2, 2, 1]
    head = ListNode.build_linked_list([1, 2, 2, 1])
    assert Solution.isPalindrome(head) is True

    # Input: head = [1, 2]
    head = ListNode.build_linked_list([1, 2])
    assert Solution.isPalindrome(head) is False

    # Input: head = [1, 2, 3, 2, 1]
    head = ListNode.build_linked_list([1, 2, 3, 2, 1])
    assert Solution.isPalindrome(head) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
