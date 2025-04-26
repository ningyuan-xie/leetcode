"""232. Implement Queue using Stacks
Link: https://leetcode.com/problems/implement-queue-using-stacks/
Difficulty: Easy
Description: Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
• void push(int x) Pushes element x to the back of the queue.
• int pop() Removes the element from the front of the queue and returns it.
• int peek() Returns the element at the front of the queue.
• boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
• You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
• Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations."""


class MyQueue:
    """Optimal Solution: Two Stacks. Time Complexity: O(n), Space Complexity: O(n)."""

    def __init__(self):
        """Constructor: instance variable stack1 and stack2 are lists"""
        self.stack1 = []  # stack1 is used to push elements
        self.stack2 = []  # stack2 is used to pop elements

    def push(self, x: int) -> None:
        """Push: append an element to the queue."""
        self.stack1.append(x)

    def pop(self) -> int:
        """Pop: remove and return the first element in the queue by moving all elements from stack1 to stack2"""
        self.peek()  # peek() will move all elements from stack1 to stack2 and reverse the order
        return self.stack2.pop()

    def peek(self) -> int:
        """Peek: look at and return the first element in the queue without removing it by moving all elements from stack1 to stack2 and reversing the order"""
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Order of elements in stack2 is now reversed
        return self.stack2[-1]

    def empty(self) -> bool:
        """Empty: check if the queue is empty by checking if both stacks are empty."""
        return not self.stack1 and not self.stack2


def unit_tests():
    # Input: ["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []], Output: [null, null, null, 1, 1, false]
    queue = MyQueue()
    assert queue.push(1) is None
    assert queue.push(2) is None
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert not queue.empty()


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
