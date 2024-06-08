# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy
# Description: Given the head of a sorted linked list, 
# delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def deleteDuplicates(head: ListNode) -> ListNode:
        # Base case: if the linked list is empty, return None
        if not head:
            return None
        
        # Initialize the current node as the head of the linked list
        current = head
        
        # Traverse the linked list
        while current:
            # If the current node and the next node have the same value
            if current.next and current.val == current.next.val:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
                
        return head


# Unit Test: Input: head = [1,1,2], Output: [1,2]
list1 = ListNode(1)
list1.next = ListNode(1)
list1.next.next = ListNode(2)
list2 = Solution.deleteDuplicates(list1)
assert list2.val == 1
assert list2.next.val == 2
print("All unit tests are passed")
