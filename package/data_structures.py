"""This script stores the data structures used in the LeetCode problems"""

from typing import List, Optional


class ListNode:
    """Class for a singly-linked list node"""

    def __init__(self, val=0, next=None):
        """Constructor for a singly-linked list node"""
        self.val = val
        self.next = next

    # Class attributes to control different equality behavior
    identity_check = False  # Default version: check the full value of the node

    def __eq__(self, other):
        """Instance equality method: overload the __eq__ method to compare two ListNode objects"""
        if ListNode.identity_check:
            # 0141-Linked-List-Cycle.py, 0160-Intersection-of-Two-Linked-Lists.py
            return self is other if isinstance(other, ListNode) else False
        return (self.val == other.val
                and self.next == other.next) if isinstance(other, ListNode) else False

    def __str__(self):
        """Instance description method: override the __str__ method"""
        return f"ListNode({self.val}, {self.next})"

    @staticmethod
    def build_linked_list(array: List) -> Optional['ListNode']:
        """Helper function to build a linked list from a list"""
        # Base Case: If the array is empty, return None
        if not array:
            return None

        # Initialize the head node and the current node
        current = head = ListNode(array[0])
        # Traverse the rest of the elements
        for val in array[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def printLinkedList(head):
        """Static method: helper function to print the linked list"""
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")


class TreeNode:
    """Class for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        """Constructor for a binary tree node"""
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        """Instance equality method: override the __eq__ method to compare two TreeNode objects"""
        return (self.val == other.val
                and self.left == other.left
                and self.right == other.right) if isinstance(other, TreeNode) else False

    def __str__(self):
        """Instance description method: override the __str__ method"""
        return f"TreeNode({self.val}, {self.left}, {self.right})"

    @staticmethod
    def build_binary_tree(array: List) -> Optional['TreeNode']:
        """Helper function to build a binary tree from a list: BFS level order traversal.
           E.g. [4, 2, 9, 3, 5, None, 7]
           -> pop 4, append 2, 9 -> pop 2, append 3, 5 -> pop 9, append 7"""
        if not array:
            return None

        # Initialize the root node, the queue, and the index
        root = TreeNode(array[0])
        queue = [root]  # queue is FIFO
        index = 1  # Start after the root element

        # Get the current node (parent) and build its two children
        while index < len(array):
            current = queue.pop(0)  # FIFO: 1st element is the new parent

            # Left child
            if index < len(array) and array[index] is not None:
                # cannot use "and array[index]" here, which will treat node 0 as False
                current.left = TreeNode(array[index])
                queue.append(current.left)
            index += 1

            # Right child
            if index < len(array) and array[index] is not None:
                current.right = TreeNode(array[index])
                queue.append(current.right)
            index += 1

        return root


class Node:
    """Class for an N-ary tree node"""

    def __init__(self, val=None, children=None):
        """Constructor for an N-ary tree node"""
        self.val = val
        self.children = children if children else []  # Still iterable when children is None

    def __eq__(self, other):
        """Instance equality method: override the __eq__ method to compare two Node objects"""
        return (self.val == other.val
                and self.children == other.children) if isinstance(other, Node) else False

    def __str__(self):
        """Instance description method: override the __str__ method"""
        return f"Node({self.val}, {self.children})"

    def __repr__(self):
        """Instance representation method: override the __repr__ method,
           which is more official than the __str__ method.
           If children is a list of nodes, it will recursively call __str__ on each
           child node, providing a clear and complete representation of the entire tree"""
        return self.__str__()

    @staticmethod
    def build_nary_tree(array: List) -> Optional['Node']:
        """Helper function to build an N-ary tree from a list: BFS level order traversal.
           E.g. [1, None, 3, 2, 4, None, 5, 6] -> pop 1, append 3, 2, 4 -> pop 3, append 5, 6"""
        # Base Case: If the array is empty, return None
        if not array:
            return None

        # Initialize the root node, the queue, and the index
        root = Node(array[0])
        queue = [root]  # queue is FIFO
        index = 2  # Start after the root element and a None

        # Outer loop: Get the current node (parent) and initialize its children
        while index < len(array):
            current = queue.pop(0)  # FIFO: 1st element is the new parent
            children = []

            # Inner loop: Process the current node's children
            while index < len(array) and array[index] is not None:  # Stop at None
                child = Node(array[index])
                children.append(child)
                queue.append(child)  # Add child to the queue for future processing
                index += 1  # Move to the next element

            # Children list completed, assign it to the current node (parent)
            current.children = children  # Assign children to the current node (parent)
            index += 1  # Skip None

        return root
