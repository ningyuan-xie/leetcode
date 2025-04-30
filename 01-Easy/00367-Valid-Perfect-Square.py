"""367. Valid Perfect Square
Link: https://leetcode.com/problems/valid-perfect-square/
Difficulty: Easy
Description: Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt."""


class Solution:
    @staticmethod
    def isPerfectSquare(num: int) -> bool:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1).
        Similar to 69. Sqrt(x)."""
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the loop ends, it means num is not a perfect square
        return False


def unit_tests():
    # Input: num = 16, Output: True
    assert Solution.isPerfectSquare(16) is True

    # Input: num = 14, Output: False
    assert Solution.isPerfectSquare(14) is False

    # Input: num = 1, Output: True
    assert Solution.isPerfectSquare(1) is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
