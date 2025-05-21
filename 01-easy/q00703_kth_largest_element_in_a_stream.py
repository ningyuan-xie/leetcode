"""703. Kth Largest Element in a Stream
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy
Description: You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.
You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.
Implement the KthLargest class:
• KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
• int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far."""

import heapq  # Priority Queue (Heap) Module


class KthLargest:
    """Optimal Solution: Min Heap. Time Complexity: O(nlog(k)), Space Complexity: O(k)."""

    def __init__(self, k: int, nums: list[int]):
        """Constructor: create a min heap of size k."""
        self.k = k
        self.min_heap = []

        # Iterate through the list of numbers and update the min heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """Add the number to the min heap and return the kth largest element through heappush and heappop operations."""
        # heappush (insert): add the new element to the end of the list, and then "bubbles up" this element to its correct position to maintain the min heap property
        heapq.heappush(self.min_heap, val)

        # heappop (extractMin): remove the smallest element from the root, move the last value to the root, and "heapify" it (exchange with lesser child) down to maintain the min heap property
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return the 1st element of the min heap, which is the minimum and the kth largest element
        return self.min_heap[0]


def unit_tests():
    # Input: ["KthLargest", "add", "add", "add", "add", "add"] [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]], Output: [null, 4, 5, 5, 8, 8]
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8

    # Input: ["KthLargest", "add", "add", "add", "add"] [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]], Output: [null, 7, 7, 7, 8]
    kth_largest = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert kth_largest.add(2) == 7
    assert kth_largest.add(10) == 7
    assert kth_largest.add(9) == 7
    assert kth_largest.add(9) == 8


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
