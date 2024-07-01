# Link: https://leetcode.com/problems/implement-stack-using-queues/
# Difficulty: Easy
# Description: Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).


class MyStack:
    # Constructor: instance variable queue is a list
    def __init__(self):
        self.queue = []

    # Push an element to the stack by appending it to the list
    def push(self, x: int) -> None:
        self.queue.append(x)

    # Pop an element from the stack by removing the last element from the list
    def pop(self) -> int:
        return self.queue.pop()

    # Top of the stack is the last element in the list
    def top(self) -> int:
        return self.queue[-1]

    # Check if the stack is empty by checking if the list is empty
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
