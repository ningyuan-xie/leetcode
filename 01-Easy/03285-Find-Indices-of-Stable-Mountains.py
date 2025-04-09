"""3285. Find Indices of Stable Mountains
Link: https://leetcode.com/problems/find-indices-of-stable-mountains/
Difficulty: Easy
Description: There are n mountains in a row, and each mountain has a height. You are given an integer array height where height[i] represents the height of mountain i, and an integer threshold.
A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. Note that mountain 0 is not stable.
Return an array containing the indices of all stable mountains in any order."""

from typing import List


class Solution:
    @staticmethod
    def stableMountains(height: List[int], threshold: int) -> List[int]:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize an empty list to store the indices of stable mountains
        stable_mountains = []

        # Iterate through the height array starting from index 1
        for i in range(1, len(height)):
            # Check if the current mountain is stable
            if height[i - 1] > threshold:
                stable_mountains.append(i)

        return stable_mountains


# Unit Test: height = [1,2,3,4,5], threshold = 2, Output: [3, 4]
assert Solution.stableMountains([1, 2, 3, 4, 5], 2) == [3, 4]

# Unit Test: height = [10,1,10,1,10], threshold = 3, Output: [1, 3]
assert Solution.stableMountains([10, 1, 10, 1, 10], 3) == [1, 3]

# Unit Test: height = [10,1,10,1,10], threshold = 10, Output: []
assert Solution.stableMountains([10, 1, 10, 1, 10], 10) == []

print("All unit tests are passed.")
