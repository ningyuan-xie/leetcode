"""1566. Detect Pattern of Length M Repeated K or More Times
Link: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times
Difficulty: Easy
Description: Given an array of positive integers arr, find a pattern of length m that is repeated
k or more times.
A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated
multiple times consecutively without overlapping. A pattern is defined by its length and the number
of repetitions.
Return true if there exists a pattern of length m that is repeated k or more times, otherwise
return false."""

from typing import List


class Solution:
    @staticmethod
    def containsPattern(arr: List[int], m: int, k: int) -> bool:
        """Optimal Solution: Pattern Matching. Time Complexity: O(n), Space Complexity: O(1)"""

        def is_repeated_pattern(start: int, length: int, repeats: int) -> bool:
            """Helper function to check if the pattern starting at `start` repeats `k` times"""
            # Outer loop: iterate over each element in the subarray of length `m`
            for subarray_element in range(length):
                # Inner loop: compare each element in the current subarray with the corresponding
                # element in the next subarrays
                for repeat in range(1, repeats):
                    if (arr[start + subarray_element] !=
                            arr[start + subarray_element + repeat * length]):
                        return False
            return True

        # Iterate through the array and check each possible starting point
        for i in range(len(arr) - m * k + 1):  # E.g. len(arr) = 6, m = 1, k = 3 -> range(4)
            if is_repeated_pattern(i, m, k):
                return True

        return False


# Unit Test: arr = [1, 2, 4, 4, 4, 4], m = 1, k = 3, Output: True
assert Solution.containsPattern([1, 2, 4, 4, 4, 4], 1, 3) is True

# Unit Test: arr = [1, 2, 1, 2, 1, 1, 1, 3], m = 2, k = 2, Output: True
assert Solution.containsPattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2) is True

# Unit Test: arr = [1, 2, 1, 2, 1, 3], m = 2, k = 3, Output: False
assert Solution.containsPattern([1, 2, 1, 2, 1, 3], 2, 3) is False

print("All unit tests are passed")
