# Link: https://leetcode.com/problems/valid-perfect-square/
# Difficulty: Easy
# Description: Given a positive integer num, write a function which returns True
# if num is a perfect square else False.

class Solution:
    # Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)
    # Similar to 0069-Sqrt(x).py and 0278-First-Bad-Version.py
    @staticmethod
    def isPerfectSquare(num: int) -> bool:
        # Base case: 0 and 1 are perfect squares
        if num < 2:
            return True
        # Initialize the left and right pointers for binary search
        left, right = 2, num  # E.g., num = 16 -> left = 2, right = 16
        # Loop until the left pointer is less than or equal to the right pointer
        while left <= right:
            # Calculate the middle pointer
            mid = (left + right) // 2
            # Calculate the square of the middle pointer
            square = mid ** 2
            # If the square is equal to the number, return True
            if square == num:
                return True
            # If the square is less than the number, move the left pointer to the middle pointer + 1
            elif square < num:
                left = mid + 1
            # If the square is greater than the number, move the right pointer to the middle pointer - 1
            else:
                right = mid - 1
        return False


# Unit Test: Input: num = 16, Output: True
# Explanation: 16 is a perfect square because 4 * 4 = 16
assert Solution.isPerfectSquare(16) == True

# Unit Test: Input: num = 14, Output: False
# Explanation: 14 is not a perfect square
assert Solution.isPerfectSquare(14) == False

# Unit Test: Input: num = 1, Output: True
# Explanation: 1 is a perfect square because 1 * 1 = 1
assert Solution.isPerfectSquare(1) == True

print("All unit tests are passed")
