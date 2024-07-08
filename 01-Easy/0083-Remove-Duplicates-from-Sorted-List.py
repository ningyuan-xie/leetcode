# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy
# Description: Given the head of a sorted linked list, 
# delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

from typing import Optional
from package.data_structures import ListNode


class Solution:
    # Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the linked list is empty, return None
        if not head:
            return None
        # Initialize the current node as the head of the linked list
        current = head
        # Iterate through the linked list
        while current.next:
            # If the current node and the next node have the same value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        return head


# Unit Test: Input: head = [1,1,2], Output: [1,2]
head_test = ListNode(1, ListNode(1, ListNode(2)))
result = Solution.deleteDuplicates(head_test)
# Two ways to print the linked list result
print(result)
ListNode.printLinkedList(result)
assert result == ListNode(1, ListNode(2))

print("All unit tests are passed")
