"""350. Intersection of Two Arrays II
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Difficulty: Easy
Description: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order."""

from typing import List


class Solution:
    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        """Optimal Solution: Hash Table. Time Complexity: O(n + m), Space Complexity: O(n).
        Similar to 242. Valid Anagram."""
        # Create a dictionary to count occurrences of each number in nums1
        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        # Create a list to store the intersection
        intersection = []

        # Iterate through nums2 and check if the number is in the count dictionary
        for num in nums2:
            if num in count and count[num] > 0:
                intersection.append(num)
                count[num] -= 1
        return intersection


def unit_tests():
    # Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], Output: [2, 2]
    assert Solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]

    # Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4], Output: [9, 4]
    assert Solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
