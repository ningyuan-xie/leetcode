# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Description: Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List


class Solution:
    # Boyer-Moore Voting Algorithm: Because this majority element occurs more than
    # n/2 (floor value) times, even if other elements will 'vote against it', it will win
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        # Initialize the majority element and its count
        majority_element, majority_count = 0, 0

        # Traverse the array to find the majority element
        for num in nums:
            # If the majority count is zero, the previous majority count is canceled out
            # and the current number could be the majority element
            if majority_count == 0:
                majority_element = num
            # When a new number appears, cancels out one current majority count
            # because this new number might actually be the majority element
            majority_count += (1 if num == majority_element else -1)

        return majority_element


# Unit Test: Input: nums = [3,2,3], Output: 3
assert Solution.majorityElement([3, 2, 3]) == 3

# Unit Test: Input: nums = [2,2,1,1,1,2,2], Output: 2
assert Solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

# Unit Test: Input: nums = [1], Output: 1
assert Solution.majorityElement([1]) == 1

print("All unit tests are passed")
