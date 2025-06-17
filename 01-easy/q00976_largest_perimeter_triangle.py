"""976. Largest Perimeter Triangle
Link: https://leetcode.com/problems/largest-perimeter-triangle/
Difficulty: Easy
Description: Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0."""

from typing import List


class Solution:
    @staticmethod
    def largestPerimeter(nums: List[int]) -> int:
        """Optimal Solution: Greedy with Early Termination. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        nums.sort(reverse=True)
        
        # We only need to check consecutive triplets after sorting
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            # Triangle inequality theorem check
            if a < b + c:
                return a + b + c
                
        return 0  # No valid triangle found


def unit_tests():
    # Input: [2,1,2], Output: 5
    assert Solution.largestPerimeter([2, 1, 2]) == 5

    # Input: [1,2,1], Output: 0
    assert Solution.largestPerimeter([1, 2, 1]) == 0

    # Input: [3,2,3,4], Output: 10
    assert Solution.largestPerimeter([3, 2, 3, 4]) == 10

    # Input: [3,6,2,3], Output: 8
    assert Solution.largestPerimeter([3, 6, 2, 3]) == 8


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
