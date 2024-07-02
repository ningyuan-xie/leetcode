# Link: https://leetcode.com/problems/implement-stack-using-queues/
# Difficulty: Easy
# Description: Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
from collections import deque


# Similar to 0232-Implement-Queue-using-Stacks.py, we can implement a stack using one queue.
class MyStack:
    # Constructor: instance variable queue is a double-ended queue
    def __init__(self):
        self.queue = deque()

    # Push: append an element to the stack.
    # Last element in the list is the top of the stack
    def push(self, x: int) -> None:
        self.queue.append(x)

    # Pop: remove and return the last element in the stack
    def pop(self) -> int:
        return self.queue.pop()

    # Top: return the last element in the stack, which is the top of the stack
    def top(self) -> int:
        return self.queue[-1]

    # Empty: check if the stack is empty by checking if the queue is empty
    def empty(self) -> bool:
        return len(self.queue) == 0


# Unit Test: Input: ["MyStack", "push", "push", "top", "pop", "empty"]
stack = MyStack()
assert stack.push(1) is None
assert stack.push(2) is None
assert stack.top() == 2
assert stack.pop() == 2
assert not stack.empty()

print("All unit tests are passed")
