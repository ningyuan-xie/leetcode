"""225. Implement Stack using Queues
Link: https://leetcode.com/problems/implement-stack-using-queues/
Difficulty: Easy
Description: Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack
(push, top, pop, and empty)."""

from collections import deque


class MyStack:
    """Optimal Solution: One Queue. Time Complexity: O(n), Space Complexity: O(n).
       Similar to 0232-Implement-Queue-using-Stacks.py, we can implement a stack using one queue"""

    def __init__(self):
        """Constructor: instance variable queue is a double-ended queue"""
        self.queue = deque()

    def push(self, x: int) -> None:
        """Push: append an element to the stack.
           Last element in the list is the top of the stack"""
        self.queue.append(x)

    def pop(self) -> int:
        """Pop: remove and return the last element in the stack"""
        return self.queue.pop()

    def top(self) -> int:
        """Top: return the last element in the stack, which is the top of the stack"""
        return self.queue[-1]

    def empty(self) -> bool:
        """Empty: check if the stack is empty by checking if the queue is empty"""
        return len(self.queue) == 0


# Input: ["MyStack", "push", "push", "top", "pop", "empty"]
stack = MyStack()
assert stack.push(1) is None
assert stack.push(2) is None
assert stack.top() == 2
assert stack.pop() == 2
assert not stack.empty()

print("All unit tests are passed.")
