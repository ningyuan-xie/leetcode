"""169. Majority Element
Link: https://leetcode.com/problems/majority-element/
Difficulty: Easy
Description: Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Follow-up: Could you solve the problem in linear time and in O(1) space?"""

from typing import List


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        """Optimal Solution: Boyer-Moore Voting Algorithm. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the candidate and count
        candidate = None
        count = 0

        for num in nums:
            # If count is zero, set the current number as the candidate
            if count == 0:
                candidate = num
            # Increment or decrement the count based on the current number
            count += (1 if num == candidate else -1)

        return candidate


def unit_tests():
    # Input: nums = [3,2,3], Output: 3
    assert Solution.majorityElement([3, 2, 3]) == 3

    # Input: nums = [2,2,1,1,1,2,2], Output: 2
    assert Solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

    # Input: nums = [1], Output: 1
    assert Solution.majorityElement([1]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
