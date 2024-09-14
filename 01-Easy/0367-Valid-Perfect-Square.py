"""367. Valid Perfect Square
Link: https://leetcode.com/problems/valid-perfect-square/
Difficulty: Easy
Description: Given a positive integer num, write a function which returns True
if num is a perfect square else False."""


class Solution:
    @staticmethod
    def isPerfectSquare(num: int) -> bool:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1).
           Similar to 0069-Sqrt(x).py"""
        # Base case: 0 and 1 are perfect squares
        if num < 2:
            return True
        # Initialize the left and right pointers for binary search
        left, right = 2, num  # E.g., num = 16 -> left = 2, right = 16
        # Loop until left pointer > right pointer
        while left <= right:
            mid = left + (right - left) // 2
            # Calculate the square of the middle pointer
            mid_squared = mid ** 2
            if mid_squared == num:
                return True
            # The square of the middle is less than the number, so the number is on the right side
            elif mid_squared < num:
                left = mid + 1
            # The square of the middle is greater than the number, so the number is on the left side
            else:
                right = mid - 1
        return False


# Unit Test: Input: num = 16, Output: True
# Explanation: 16 is a perfect square because 4 * 4 = 16
assert Solution.isPerfectSquare(16) is True

# Unit Test: Input: num = 14, Output: False
# Explanation: 14 is not a perfect square
assert Solution.isPerfectSquare(14) is False

# Unit Test: Input: num = 1, Output: True
# Explanation: 1 is a perfect square because 1 * 1 = 1
assert Solution.isPerfectSquare(1) is True

print("All unit tests are passed")
