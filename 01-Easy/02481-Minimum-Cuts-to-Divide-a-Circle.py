"""2481. Minimum Cuts to Divide a Circle
Link: https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/
Difficulty: Easy
Description: A valid cut in a circle can be:
- A cut that is represented by a straight line that touches two points on the edge of the circle and
passes through its center, or
- A cut that is represented by a straight line that touches one point on the edge of the circle and
its center.
Some valid and invalid cuts are shown in the figures below.
Given the integer n, return the minimum number of cuts needed to divide a circle into n equal slices."""


class Solution:
    @staticmethod
    def numberOfCuts(n: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # Base case: no cuts needed for 1 slice
        if n == 1:
            return 0
        # If n is even, we need n/2 cuts
        elif n % 2 == 0:
            return n // 2
        # If n is odd, we need n cuts
        else:
            return n


# Unit Test: n = 4, Output: 2
assert Solution.numberOfCuts(4) == 2

# Unit Test: n = 3, Output: 3
assert Solution.numberOfCuts(3) == 3

print("All unit tests are passed.")
