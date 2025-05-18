"""2485. Find the Pivot Integer
Link: https://leetcode.com/problems/find-the-pivot-integer/
Difficulty: Easy
Description: Given a positive integer n, find the pivot integer x such that:
- The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n
inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be
at most one pivot index for the given input."""


class Solution:
    @staticmethod
    def pivotInteger(n: int) -> int:
        """Optimal Solution: Prefix Sum. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 724. Find Pivot Index"""
        # Compute the total sum of the nums
        total_sum = sum(range(1, n + 1))

        # Initialize the left sum to 0
        left_sum = 0

        # Start from 1 to n
        for i in range(1, n + 1):
            # Check if the left sum == right sum (both inclusively)
            if left_sum + i == total_sum - left_sum:
                return i
            # Update the left sum
            else:
                left_sum += i

        return -1


# Unit Test: n = 8, Output: 6
assert Solution.pivotInteger(8) == 6

# Unit Test: n = 1, Output: 1
assert Solution.pivotInteger(1) == 1

# Unit Test: n = 4, Output: -1
assert Solution.pivotInteger(4) == -1

print("All unit tests are passed.")
