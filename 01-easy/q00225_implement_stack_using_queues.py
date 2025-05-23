"""225. Implement Stack using Queues
Link: https://leetcode.com/problems/implement-stack-using-queues/
Difficulty: Easy
Description: Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
• void push(int x) Pushes element x to the top of the stack.
• int pop() Removes the element on the top of the stack and returns it.
• int top() Returns the element on the top of the stack.
• boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
• You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
• Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations."""

from collections import deque


class MyStack:
    """Optimal Solution: One Queue. Time Complexity: O(n), Space Complexity: O(n)."""

    def __init__(self):
        """Constructor: instance variable queue is a double-ended queue."""
        self.queue = deque()

    def push(self, x: int) -> None:
        """Push: append an element to the stack. Last element in the list is the top of the stack."""
        self.queue.append(x)

    def pop(self) -> int:
        """Pop: remove and return the last element in the stack."""
        return self.queue.pop()

    def top(self) -> int:
        """Top: return the last element in the stack, which is the top of the stack."""
        return self.queue[-1]

    def empty(self) -> bool:
        """Empty: check if the stack is empty by checking if the queue is empty."""
        return len(self.queue) == 0


def unit_tests():
    # Input: ["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []], Output: [null, null, null, 2, 2, false]
    stack = MyStack()
    assert stack.push(1) is None
    assert stack.push(2) is None
    assert stack.top() == 2
    assert stack.pop() == 2
    assert not stack.empty()


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
