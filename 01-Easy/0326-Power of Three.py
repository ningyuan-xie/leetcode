# Link: https://leetcode.com/problems/power-of-three/
# Difficulty: Easy
# Description: Given an integer n, return true if it is a power of three. Otherwise, return false.
# Follow up: Could you solve it without loops/recursion?

class Solution:
    # Optimal Solution: Math (only for prime). Time Complexity: O(1), Space Complexity: O(1)
    # Similar to 0231-Power-of-Two.py
    @staticmethod
    def isPowerOfThree(n: int) -> bool:
        # The maximum power of 3 that can be stored in a 32-bit integer is 3^19 = 1162261467
        return n > 0 and (3**19) % n == 0

    # Alternative Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n))
    # Similar to 0231-Power-of-Two.py
    @staticmethod
    def isPowerOfThreeRecursion(n: int) -> bool:
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # Base case: if n is equal to 1, return True
        if n == 1:
            return True
        # If n is divisible by 3, then recursively check if n // 3 is a power of 3
        return n % 3 == 0 and Solution.isPowerOfThreeRecursion(n // 3)


# Unit Test: Input: n = 27, Output: True
assert Solution.isPowerOfThree(27) is True

# Unit Test: Input: n = 0, Output: False
assert Solution.isPowerOfThree(0) is False

# Unit Test: Input: n = 9, Output: True
assert Solution.isPowerOfThreeRecursion(9) is True

# Unit Test: Input: n = 45, Output: False
assert Solution.isPowerOfThreeRecursion(45) is False

print("All unit tests are passed")
