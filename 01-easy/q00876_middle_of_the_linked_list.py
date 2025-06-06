"""876. Middle of the Linked List
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy
Description: Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node."""

from package.data_structures import ListNode


class Solution:
    @staticmethod
    def middleNode(head: ListNode) -> ListNode:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 141. Linked List Cycle and 234. Palindrome Linked List."""
        # Initialize two pointers: slow and fast
        slow = fast = head
        # Traverse the linked list with two pointers
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Return slow which is the middle node
        return slow


def unit_tests():
    # Input: head = [1,2,3,4,5], Output: [3,4,5]
    head = ListNode.build_linked_list([1, 2, 3, 4, 5])
    output = ListNode.build_linked_list([3, 4, 5])
    assert Solution.middleNode(head) == output

    # Input: head = [1,2,3,4,5,6], Output: [4,5,6]
    head = ListNode.build_linked_list([1, 2, 3, 4, 5, 6])
    output = ListNode.build_linked_list([4, 5, 6])
    assert Solution.middleNode(head) == output


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
