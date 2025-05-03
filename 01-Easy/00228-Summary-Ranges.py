"""228. Summary Ranges
Link: https://leetcode.com/problems/summary-ranges/
Difficulty: Easy
Description: You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
• "a->b" if a != b
• "a" if a == b"""

from typing import List


class Solution:
    @staticmethod
    def summaryRanges(nums: List[int]) -> List[str]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)."""
        # Base case: if the input list is empty, return an empty list
        if not nums:
            return []

        n = len(nums)
        result = []
        start = end = nums[0]
        
        for i in range(1, n):
            # If the current number is consecutive to the previous number
            if nums[i] == end + 1:
                # Update the end of the range without updating the start
                end = nums[i]
            else:
                # Stop the range and add it to the result list
                if start == end:
                    result.append(str(start))  # single number
                else:
                    result.append(f"{start}->{end}")  # range of numbers
                # Update both start and end to the current number
                start = end = nums[i]
        
        # Add the last range to the result list because the loop ends before adding it
        if start == end:
            result.append(str(start))  # single number
        else:
            result.append(f"{start}->{end}")  # range of numbers
        return result


def unit_tests():
    # Input: [0, 1, 2, 4, 5, 7], Output: ["0->2","4->5","7"]
    nums = [0, 1, 2, 4, 5, 7]
    assert Solution.summaryRanges(nums) == ["0->2", "4->5", "7"]

    # Input: [0, 2, 3, 4, 6, 8, 9], Output: ["0","2->4","6","8->9"]
    nums = [0, 2, 3, 4, 6, 8, 9]
    assert Solution.summaryRanges(nums) == ["0", "2->4", "6", "8->9"]

    # Input: [], Output: []
    nums = []
    assert Solution.summaryRanges(nums) == []


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
