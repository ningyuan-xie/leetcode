"""977. Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy
Description: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?"""

from typing import List


class Solution:
    @staticmethod
    def sortedSquares(nums: List[int]) -> List[int]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)."""
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1

        # Loop through the result array in reverse order
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result


def unit_tests():
    # Input: [-4,-1,0,3,10], Output: [0,1,9,16,100]
    assert Solution.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

    # Input: [-7,-3,2,3,11], Output: [4,9,9,49,121]
    assert Solution.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
