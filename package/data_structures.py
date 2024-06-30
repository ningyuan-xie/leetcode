# This script stores the data structures used in the LeetCode problems.

# Definition for singly-linked list
class ListNode:
    # Constructor
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Override the __eq__ method to compare two ListNode objects
    def __eq__(self, other):
        return self.val == other.val and self.next == other.next if other else False

    # Class description method: override the __str__ method
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

    # Helper function to print the linked list
    @staticmethod
    def printLinkedList(head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")


# Definition for a binary tree node
class TreeNode:
    # Constructor
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Class description method: override the __str__ method
    def __str__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"





