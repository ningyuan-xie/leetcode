"""2032. Two Out of Three
Link: https://leetcode.com/problems/two-out-of-three/
Difficulty: Easy
Description: Given three integer arrays nums1, nums2, and nums3, return a distinct array
containing all the values that are present in at least two out of the three arrays.
You may return the values in any order."""

from typing import List


class Solution:
    @staticmethod
    def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        """Optimal Solution: Set Intersection. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the set to store the distinct values that are present in at least two out of
        # the three arrays
        result = set()

        # Initialize the set for each array
        set1 = set(nums1)  # E.g. nums1 = [1, 1, 3, 2] -> set1 = {1, 2, 3}
        set2 = set(nums2)  # E.g. nums2 = [2, 3] -> set2 = {2, 3}
        set3 = set(nums3)  # E.g. nums3 = [3] -> set3 = {3}

        # Find the intersection of the sets
        result.update(set1 & set2)  # .update() adds the elements of the set to the result set
        result.update(set2 & set3)
        result.update(set1 & set3)

        return list(result)


# Unit Test: nums1 = [1, 1, 3, 2], nums2 = [2, 3], nums3 = [3], Output: [2, 3]
assert Solution.twoOutOfThree([1, 1, 3, 2], [2, 3], [3]) == [2, 3]

# Unit Test: nums1 = [3, 1], nums2 = [2, 3], nums3 = [1, 2], Output: [1, 2, 3]
assert Solution.twoOutOfThree([3, 1], [2, 3], [1, 2]) == [1, 2, 3]

# Unit Test: nums1 = [1, 2, 2], nums2 = [4, 3, 3], nums3 = [5], Output: []
assert Solution.twoOutOfThree([1, 2, 2], [4, 3, 3], [5]) == []

print("All unit tests are passed.")
