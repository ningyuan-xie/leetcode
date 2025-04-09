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
           Similar to 0141-Linked-List-Cycle.py and 0234-Palindrome-Linked-List.py"""
        # Initialize two pointers: slow and fast
        slow = fast = head
        # Traverse the linked list with two pointers
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Return slow which is the middle node
        return slow


# Unit Test: Input: head = [1,2,3,4,5], Output: [3,4,5]
head_test = ListNode.build_linked_list([1, 2, 3, 4, 5])
head_expected = ListNode.build_linked_list([3, 4, 5])
assert Solution.middleNode(head_test) == head_expected

# Unit Test: Input: head = [1,2,3,4,5,6], Output: [4,5,6]
head_test = ListNode.build_linked_list([1, 2, 3, 4, 5, 6])
head_expected = ListNode.build_linked_list([4, 5, 6])
assert Solution.middleNode(head_test) == head_expected

print("All unit tests are passed")
