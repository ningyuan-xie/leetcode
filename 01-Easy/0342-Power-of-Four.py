# Link: https://leetcode.com/problems/power-of-four/
# Difficulty: Easy
# Description: Given an integer n, return true if it is a power of four. Otherwise, return false.
# Follow up: Could you solve it without loops/recursion?

class Solution:
    # Optimal Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n))
    # Similar to 0231-Power-of-Two.py and 0326-Power-of-Three.py
    # Written in instance method format instead of static method format
    def isPowerOfFour(self, n: int) -> bool:
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # Base case: if n is equal to 1, return True
        if n == 1:
            return True
        # If n is divisible by 4, then recursively check if n // 4 is a power of 4
        # When making a recursive call within a class method,
        # do not need to explicitly pass self again as an argument
        return n % 4 == 0 and self.isPowerOfFour(n // 4)


# Unit Test: Input: n = 2, Output: False
solution = Solution()
assert solution.isPowerOfFour(2) is False

# Unit Test: Input: n = 8, Output: False
assert solution.isPowerOfFour(8) is False

# Unit Test: Input: n = 16, Output: True
assert solution.isPowerOfFour(16) is True

# Unit Test: Input: n = 5, Output: False
assert solution.isPowerOfFour(5) is False

# Unit Test: Input: n = 1, Output: True
assert solution.isPowerOfFour(1) is True

# Unit Test: Input: n = 0, Output: False
assert solution.isPowerOfFour(0) is False

print("All unit tests are passed")
