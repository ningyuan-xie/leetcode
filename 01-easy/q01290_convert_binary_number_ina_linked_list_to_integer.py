"""1290. Convert Binary Number in a Linked List to Integer
Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Difficulty: Easy
Description: Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list."""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def getDecimalValue(head: Optional[ListNode]) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        result = 0

        while head:
            result = result * 2 + head.val
            head = head.next

        return result


def unit_tests():
    # Input: head = [1, 0, 1], Output: 5
    head = ListNode.build_linked_list([1, 0, 1])
    assert Solution.getDecimalValue(head) == 5

    # Input: head = [0], Output: 0
    head = ListNode.build_linked_list([0])
    assert Solution.getDecimalValue(head) == 0

    # Input: head = [1], Output: 1
    head = ListNode.build_linked_list([1])
    assert Solution.getDecimalValue(head) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
