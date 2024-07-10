# Link: https://leetcode.com/problems/sqrtx/
# Difficulty: Easy
# Description: Given a non-negative integer x, compute and return the square root of x.

class Solution:
    # Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)
    @staticmethod
    def mySqrt(x: int) -> int:
        # Base case: if x is 0 or 1, return x
        if x == 0 or x == 1:
            return x
        # Initialize the left and right pointers
        left, right = 1, x
        while left <= right:
            # Calculate the middle value
            mid = (left + right) // 2
            # Calculate the square of the middle value
            mid_squared = mid ** 2
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
        # When the loop terminates: left > right
        # left will be the ceiling of the square root of x
        # right will be the floor of the square root of x
        return right


# Unit Test: Input: x = 4, Output: 2
assert Solution.mySqrt(4) == 2

# Unit Test: Input: x = 8, Output: 2
assert Solution.mySqrt(8) == 2

# Unit Test: Input: x = 1, Output: 1
assert Solution.mySqrt(1) == 1

print("All unit tests are passed")
