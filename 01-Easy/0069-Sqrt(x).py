"""69. Sqrt(x)
Link: https://leetcode.com/problems/sqrtx/
Difficulty: Easy
Description: Given a non-negative integer x, compute and return the square root of x."""


class Solution:
    @staticmethod
    def mySqrt(x: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Base case: if x is 0 or 1, return x
        if x == 0 or x == 1:
            return x
        # Initialize the left and right pointers
        left, right = 1, x
        # Loop until left pointer > right pointer
        while left <= right:
            # Calculate the middle value
            mid = (left + right) // 2
            # Calculate the square of the middle value
            mid_squared = mid ** 2
            if mid_squared == x:
                return mid
            # The square of the middle is less than x, so the square root is on the right side
            elif mid_squared < x:
                left = mid + 1
            # The square of the middle is greater than x, so the square root is on the left side
            else:
                right = mid - 1
        # Left is the ceiling and right is the floor of the square root of x
        return right


# Unit Test: Input: x = 4, Output: 2
assert Solution.mySqrt(4) == 2

# Unit Test: Input: x = 8, Output: 2
assert Solution.mySqrt(8) == 2

# Unit Test: Input: x = 1, Output: 1
assert Solution.mySqrt(1) == 1

print("All unit tests are passed")
