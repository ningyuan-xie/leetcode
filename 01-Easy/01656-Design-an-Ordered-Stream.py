"""1656. Design an Ordered Stream
Link: https://leetcode.com/problems/design-an-ordered-stream/
Difficulty: Easy
Description: There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey
is an integer between 1 and n and value is a string. No two pairs have the same id.
Design a stream that returns the values in increasing order of their IDs by returning a chunk (list)
of values after each insertion. The concatenation of all the chunks should result in a list of the
sorted values.
Implement the OrderedStream class:
- OrderedStream(int n) Constructs the stream to take n values.
- String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then
returns the largest possible chunk of currently inserted values that appear next in the order."""

from typing import List, Optional


class OrderedStream:
    """Optimal Solution: Array Stream. Time Complexity: O(n), Space Complexity: O(n)"""

    def __init__(self, n: int):
        """Constructor: Initialize the stream with n elements"""
        self.stream: List[Optional[str]] = [None] * n  # Specify that stream can hold strings or None
        self.ptr = 0  # Pointer to track the start of the next filled elements

    def insert(self, idKey: int, value: str) -> list[str]:
        """Insert a value into the stream and return the contiguous values"""

        # Insert the value into the stream at idKey - 1 (idKey is 1-indexed)
        self.stream[idKey - 1] = value

        # Initialize the result array
        result = []

        # Traverse the stream starting from the pointer position (self.ptr) and collect values as
        # long as there are non-None values in contiguous slots
        while (self.ptr < len(self.stream) and
               self.stream[self.ptr]):  # does not run if self.stream[self.ptr] is None
            result.append(self.stream[self.ptr])
            self.ptr += 1
        # Return the list of contiguous values starting from the pointer position
        return result


# Unit Test: n = 5, insert(3, "ccccc") -> [], insert(1, "aaaaa") -> ["aaaaa"], insert(2, "bbbbb") ->
# ["bbbbb", "ccccc"], insert(5, "eeeee") -> [], insert(4, "ddddd") -> ["ddddd", "eeeee"]
os = OrderedStream(5)
assert os.insert(3, "ccccc") == []
assert os.insert(1, "aaaaa") == ["aaaaa"]
assert os.insert(2, "bbbb") == ["bbbb", "ccccc"]
assert os.insert(5, "eeeee") == []
assert os.insert(4, "ddddd") == ["ddddd", "eeeee"]

print("All unit tests are passed.")
