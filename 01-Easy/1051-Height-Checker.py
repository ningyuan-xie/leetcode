"""1051. Height Checker
Link: https://leetcode.com/problems/height-checker/
Difficulty: Easy
Description: A school is trying to take an annual photo of all the students. The students are asked
to stand in a single file line in non-decreasing order by height. Let this ordering be represented
by the integer array expected where expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are
standing in. Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i]."""

from typing import List


class Solution:
    @staticmethod
    def heightChecker(heights: List[int]) -> int:
        """Optimal Solution: Height Distribution Check. Time Complexity: O(n), Space Complexity: O(1).
           Analyzing the distribution of heights and checking how far off they are from their
           expected order"""
        count = [0] * 101  # Count of heights (range 1-100)

        # Build frequency count for heights
        for h in heights:
            count[h] += 1  # E.g. [1, 1, 4, 2, 1, 3] -> [0, 3, 1, 1, 1, 0, ..., 0]

        mismatch_count, expected = 0, 0

        # Compare actual heights with expected sorted order
        for h in heights:
            while count[expected] == 0:
                # Skip the current expected height until we find a student with that height
                expected += 1
            if h != expected:
                mismatch_count += 1
            # Reduce the count of the expected height
            count[expected] -= 1

        return mismatch_count


# Unit Test: heights = [1, 1, 4, 2, 1, 3], Output: 3
# Explanation: The expected order is [1, 1, 1, 2, 3, 4], so indices 2, 3, and 5 do not match.
assert Solution.heightChecker([1, 1, 4, 2, 1, 3]) == 3

# Unit Test: heights = [5, 1, 2, 3, 4], Output: 5
# Explanation: The expected order is [1, 2, 3, 4, 5], so all indices do not match.
assert Solution.heightChecker([5, 1, 2, 3, 4]) == 5

# Unit Test: heights = [1, 2, 3, 4, 5], Output: 0
# Explanation: The expected order is [1, 2, 3, 4, 5], so all indices match.
assert Solution.heightChecker([1, 2, 3, 4, 5]) == 0

print("All unit tests are passed")
