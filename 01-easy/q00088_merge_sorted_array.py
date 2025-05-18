"""88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Description: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."""

from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Optimal Solution: Three Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize pointers for nums1, nums2 and the merged array
        p1, p2, last = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        for p in range(last, -1, -1):
            # If nums2 is exhausted, break
            if p2 < 0:
                break

            # If nums1 is exhausted or nums2 is greater, place nums2's element
            if p1 < 0 or nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                # Place nums1's element
                nums1[p] = nums1[p1]
                p1 -= 1


def unit_tests():
    # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3, Output: [1,2,2,3,5,6]
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # Input: nums1 = [2,2,3,0,0,0], m = 3, nums2 = [1,5,6], n = 3, Output: [1,2,2,3,5,6]
    nums1 = [2, 2, 3, 0, 0, 0]
    Solution.merge(nums1, 3, [1, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # Input: nums1 = [1], m = 1, nums2 = [], n = 0, Output: [1]
    nums1 = [1]
    Solution.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    # Input: nums1 = [0], m = 0, nums2 = [1], n = 1, Output: [1]
    nums1 = [0]
    Solution.merge(nums1, 0, [1], 1)
    assert nums1 == [1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
