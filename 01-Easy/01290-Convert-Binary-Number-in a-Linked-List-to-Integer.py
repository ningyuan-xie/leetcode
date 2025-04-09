"""1290. Convert Binary Number in a Linked List to Integer
Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Difficulty: Easy
Description: Given head which is a reference node to a singly-linked list. The value of each node
in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list."""


from package.data_structures import ListNode


class Solution:
    @staticmethod
    def getDecimalValue(head: ListNode) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the result
        result = 0

        # Traverse the linked list
        while head:
            # Update the result: result = result * 2 + head.val
            # | is the bitwise OR operator to add the new bit to the result: 0 | 0 = 0, 0 | 1 = 1
            result = (result << 1) | head.val
            head = head.next

        return result


# Unit Test: head = [1, 0, 1], Output: 5
# 1st node: head.val = 1, result = 0 * 2 + 1 = 1
# 2nd node: head.val = 0, result = 1 * 2 + 0 = 2
# 3rd node: head.val = 1, result = 2 * 2 + 1 = 5
head_test = ListNode.build_linked_list([1, 0, 1])
assert Solution.getDecimalValue(head_test) == 5

# Unit Test: head = [0], Output: 0
# 1st node: head.val = 0, result = 0 * 2 + 0 = 0
head_test = ListNode.build_linked_list([0])
assert Solution.getDecimalValue(head_test) == 0

# Unit Test: head = [1], Output: 1
# 1st node: head.val = 1, result = 0 * 2 + 1 = 1
head_test = ListNode.build_linked_list([1])
assert Solution.getDecimalValue(head_test) == 1

print("All unit tests are passed.")
