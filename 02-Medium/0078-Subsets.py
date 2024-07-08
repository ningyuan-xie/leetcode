# Link: https://leetcode.com/problems/subsets/
# Difficulty: Medium
# Description: Given an integer array nums of unique elements,
# return all possible subsets (the power set).

from typing import List


class Solution:
    # Optimal Solution: Iteration. Time Complexity: O(2^n), Space Complexity: O(2^n)
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        # Initialize the result list with an empty subset
        result = [[]]
        # Iterate through the numbers
        for n in nums:  # 1, 2, 3
            new_subsets = []
            # New subset and result have the same length, as the only difference is the new number
            for subset in result:
                new_subsets.append(subset + [n])  # [] + [1] = [1]; [] + [2] = [2], [1] + [2] = [1, 2]
                # n = 1, new_subsets: [[1]]
                # n = 2, new_subsets: [[2]] -> [[2], [1, 2]]
                # n = 3, new_subsets: [[3]] -> [[3], [1, 3]] -> ... -> [[3], [1, 3], [2, 3], [1, 2, 3]]
            # Result's size doubles: it duplicates itself and adds the new number to duplicated subsets
            result += new_subsets
            # n = 1, result: [[], [1]]
            # n = 2, result: [[], [1], [2], [1, 2]]
            # n = 3, result: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        return result


# Unit Test: Input: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert Solution.subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Unit Test: Input: nums = [0], Output: [[],[0]]
assert Solution.subsets([0]) == [[], [0]]

print("All unit tests are passed")
