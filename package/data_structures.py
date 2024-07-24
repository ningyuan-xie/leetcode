# This script stores the data structures used in the LeetCode problems.

# 1. Definition for singly-linked list
class ListNode:
    # Constructor
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Instance equality method: override the __eq__ method to compare two ListNode objects
    def __eq__(self, other):
        return (self.val == other.val
                and self.next == other.next) if other else False

    # Instance description method: override the __str__ method
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

    # Static method: helper function to print the linked list
    @staticmethod
    def printLinkedList(head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")


# 2. Definition for a binary tree node
class TreeNode:
    # Constructor
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Instance equality method: override the __eq__ method to compare two TreeNode objects
    def __eq__(self, other):
        return (self.val == other.val
                and self.left == other.left
                and self.right == other.right) if other else False

    # Instance description method: override the __str__ method
    def __str__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


# 3. Definition for a Node
class Node:
    # Constructor
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    # Instance equality method: override the __eq__ method to compare two Node objects
    def __eq__(self, other):
        return (self.val == other.val
                and self.children == other.children) if other else False

    # Instance description method: override the __str__ method
    def __str__(self):
        return f"Node({self.val}, {self.children})"

    # Instance representation method: override the __repr__ method,
    # which is more official than the __str__ method
    def __repr__(self):
        # If children is a list of nodes, it will recursively call __str__ on each
        # child node, providing a clear and complete representation of the entire tree.
        return self.__str__()

    # Helper function to build an N-ary tree from a list
    @staticmethod
    def build_nary_tree(array):  # E.g. [1, None, 3, 2, 4, None, 5, 6]
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
            while index < len(array) and array[index]:  # Stop at None
                child = Node(array[index])
                children.append(child)
                queue.append(child)  # Add child to the queue for future processing
                index += 1  # Move to the next element

            # Children list completed, assign it to the current node (parent)
            current.children = children  # Assign children to the current node (parent)
            index += 1  # Skip None

        return root
