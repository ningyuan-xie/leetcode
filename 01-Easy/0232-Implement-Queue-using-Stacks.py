# Link: https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty: Easy
# Description: Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).


# Similar to 0225-Implement-Stack-using-Queues.py, we can implement a queue using two stacks.
class MyQueue:
    # Constructor: instance variable stack1 and stack2 are lists
    def __init__(self):
        self.stack1 = []  # stack1 is used to push elements
        self.stack2 = []  # stack2 is used to pop elements

    # Push: append an element to the queue.
    # First element in the list is the first element in the queue
    def push(self, x: int) -> None:
        self.stack1.append(x)

    # Pop: remove and return the first element in the queue
    # by moving all elements from stack1 to stack2
    def pop(self) -> int:
        self.peek()  # peek() will move all elements from stack1 to stack2 and reverse the order
        return self.stack2.pop()

    # Peek: look at and return the first element in the queue without removing it
    # by moving all elements from stack1 to stack2 and reversing the order
    def peek(self) -> int:
        if not self.stack2:  # if stack2 is empty, move all elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # order of elements is now reversed in stack2
        return self.stack2[-1]

    # Empty: check if the queue is empty by checking if both stacks are empty
    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Unit Test: Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
queue = MyQueue()
assert queue.push(1) is None
assert queue.push(2) is None
assert queue.peek() == 1
assert queue.pop() == 1
assert not queue.empty()

print("All unit tests are passed")
