# Link: https://leetcode.com/problems/remove-linked-list-elements/
# Difficulty: Easy
# Description: Remove all elements from a linked list of integers that have value val.

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Initialize a dummy node to avoid edge cases
        dummy = ListNode(0)
        dummy.next = head
        # Initialize the current node as the dummy node
        current = dummy
        # Iterate through the linked list
        while current.next:
            # If the next node has the target value, skip the next node
            if current.next.val == val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        return dummy.next  # dummy: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None


# Unit Test: Input: head = [1,2,6,3,4,5,6], val = 6, Output: [1,2,3,4,5]
head_test = ListNode(1, ListNode(2, ListNode(6,
                                             ListNode(3, ListNode(4,
                                                                  ListNode(5, ListNode(6)))))))
result = Solution.removeElements(head_test, 6)
print(result)
assert result == ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Unit Test: Input: head = [], val = 1, Output: []
head_test = None
result = Solution.removeElements(head_test, 1)
print(result)
assert result is None

# Unit Test: Input: head = [7,7,7,7], val = 7, Output: []
head_test = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
result = Solution.removeElements(head_test, 7)
print(result)
assert result is None

print("All unit tests are passed")
