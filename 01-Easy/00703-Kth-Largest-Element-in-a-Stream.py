"""703. Kth Largest Element in a Stream
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy
Description: Design a class to find the kth largest element in a stream. Note that it is the
kth largest element in the sorted order, not the kth distinct element."""

import heapq  # Priority Queue (Heap) Module


class KthLargest:
    """Optimal Solution: Min Heap. Time Complexity: O(nlog(k)), Space Complexity: O(k)"""

    def __init__(self, k: int, nums: list[int]):
        """Constructor: Initialize the instance variables. Time Complexity: O(nlog(k))"""
        # Initialize the two variables
        self.k = k
        self.min_heap = []

        # Iterate through the list of numbers and update the min heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """Add the number to the min heap and return the kth largest element through
           heappush and heappop operations. Time Complexity: O(log(k))"""
        # heappush (insert): add the new element to the end of the list, and then "bubbles up" this
        # element to its correct position to maintain the min heap property
        heapq.heappush(self.min_heap, val)

        # If the size of the min heap exceeds k, remove the smallest element:
        # heappop (extractMin): remove the smallest element from the root, move the last value to the
        # root, and "heapify" it (exchange with lesser child) down to maintain the min heap property
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return the 1st element of the min heap, which is the minimum and the kth largest element
        return self.min_heap[0]


# Input: k = 3, nums = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
# Output: [null, 4, 5, 5, 8, 8]
kth_largest = KthLargest(3, [4, 5, 8, 2])  # [4, 5, 8, 2] -> [2, 4, 8, 5] -> [4, 5, 8]
assert kth_largest.add(3) == 4  # [4, 5, 8, 3] -> [3, 4, 8, 5] -> [4, 5, 8], returns 4
assert kth_largest.add(5) == 5  # [4, 5, 8, 5] -> [5, 5, 8], returns 5
assert kth_largest.add(10) == 5  # [5, 5, 8, 10] -> [5, 10, 8], returns 5
assert kth_largest.add(9) == 8  # [5, 10, 8, 9] -> [5, 9, 8, 10] -> [8, 9, 10], returns 8
assert kth_largest.add(4) == 8  # [8, 9, 10, 4] -> [4, 8, 10, 9] -> [8, 9, 10], returns 8
# Since k = 3, the heap always contain the 3 largest elements: [8, 9, 10]

# Input: k = 1, nums = [[1, []], [-3], [-2], [-4]], Output: [-3, -2, -2]
kth_largest = KthLargest(1, [])  # []
assert kth_largest.add(-3) == -3  # [-3], returns -3
assert kth_largest.add(-2) == -2  # [-3, -2] -> [-2], returns -2
assert kth_largest.add(-4) == -2  # [-2, -4] -> [-4, -2] -> [-2], returns -2
# Since k = 1, the heap always contain the 1 largest element: [-2]

print("All unit tests are passed.")
