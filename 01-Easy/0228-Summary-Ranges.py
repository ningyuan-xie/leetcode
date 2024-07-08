# Link: https://leetcode.com/problems/summary-ranges/
# Difficulty: Easy
# Description: You are given a sorted unique integer array nums.
# Return the smallest sorted list of ranges that cover all the numbers in the input array.

from typing import List


class Solution:
    # Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def summaryRanges(nums: List[int]) -> List[str]:
        # Base case: if the input list is empty, return an empty list
        if not nums:
            return []
        # Initialize the result list
        result = []
        # Initialize two pointers: start and end
        start = end = nums[0]  # start = end = 0
        for i in range(1, len(nums)):  # nums = [0, 1, 2, 4, 5, 7]
            # If the current number is consecutive to the previous number
            if nums[i] == end + 1:
                # Continue the range by shifting the end to the current number
                end = nums[i]  # end = 1, 2, 5
            else:
                # Stop the range and add it to the result list
                if start == end:
                    result.append(str(start))  # single number
                else:
                    result.append(f"{start}->{end}")  # range of numbers
                # Shift the start and end pointers to the current number
                start = end = nums[i]  # start = end = 4, 7
        # Add the last range to the result list because the loop ends before adding it
        if start == end:
            result.append(str(start))  # single number
        else:
            result.append(f"{start}->{end}")  # range of numbers
        return result


# Unit Test: Input: [0, 1, 2, 4, 5, 7]
nums_test = [0, 1, 2, 4, 5, 7]
assert Solution.summaryRanges(nums_test) == ["0->2", "4->5", "7"]

# Unit Test: Input: [0, 2, 3, 4, 6, 8, 9]
nums_test = [0, 2, 3, 4, 6, 8, 9]
assert Solution.summaryRanges(nums_test) == ["0", "2->4", "6", "8->9"]

# Unit Test: Input: []
nums_test = []
assert Solution.summaryRanges(nums_test) == []

print("All unit tests are passed")
