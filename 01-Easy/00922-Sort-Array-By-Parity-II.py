"""922. Sort Array By Parity II
Link: https://leetcode.com/problems/sort-array-by-parity-ii/
Difficulty: Easy
Description: Given an array of integers nums, half of the integers in nums are odd, and the other
half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition."""

from typing import List


class Solution:
    @staticmethod
    def sortArrayByParityII(nums: List[int]) -> List[int]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0905-Sort-Array-By-Parity.py"""
        # Initialize the two pointers
        even, odd = 0, 1

        # Move the even integers to the left and the odd integers to the right
        while even < len(nums) and odd < len(nums):
            # If even index is even, skip it, and +2 to disregard the ignored even integer
            if nums[even] % 2 == 0:
                even += 2
            # If odd index is odd, skip it, and +2 to disregard the ignored odd integer
            elif nums[odd] % 2 == 1:
                odd += 2
            # Otherwise, swap even and odd, and +2 to disregard the swapped even and odd integers
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2

        return nums


# Unit Test: Input: nums = [4,2,5,7], Output: [4,5,2,7]
assert Solution.sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7]

# Unit Test: Input: nums = [2,3], Output: [2,3]
assert Solution.sortArrayByParityII([2, 3]) == [2, 3]

# Unit Test: Input: nums = [3,2], Output: [2,3]
assert Solution.sortArrayByParityII([3, 2]) == [2, 3]

# Unit Test: Input: nums = [3,2,4,1], Output: [2,3,4,1]
assert Solution.sortArrayByParityII([3, 2, 4, 1]) == [2, 3, 4, 1]

print("All unit tests are passed")
