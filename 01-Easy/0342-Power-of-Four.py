# Link: https://leetcode.com/problems/power-of-four/
# Difficulty: Easy
# Description: Given an integer n, return true if it is a power of four. Otherwise, return false.
# Follow up: Could you solve it without loops/recursion?

class Solution:
    # Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)
    # Similar to 0231-Power-of-Two.py and 0326-Power-of-Three.py
    @staticmethod
    def isPowerOfFour(n: int) -> bool:
        # The maximum power of 4 that can be stored in a 32-bit integer is 4^15 = 1073741824
        return n > 0 and (4**15) % n == 0

    # Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)
    # Similar to 0231-Power-of-Two.py
    @staticmethod
    def isPowerOfFourBit(n: int) -> bool:
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # If n is a power of 4, then n only has 1 bit = 1, and the bit is at an odd index
        # E.g. 4 (100) & 5 (101) = 4 (100), 16 (10000) & 17 (10001) = 16 (10000)
        return n & (n - 1) == 0 and n & 0x55555555 != 0

    # Alternative Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n))
    # Similar to 0231-Power-of-Two.py and 0326-Power-of-Three.py
    @staticmethod
    def isPowerOfFourRecursion(n: int) -> bool:
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # Base case: if n is equal to 1, return True
        if n == 1:
            return True
        # If n is divisible by 4, then recursively check if n // 4 is a power of 4
        return n % 4 == 0 and Solution.isPowerOfFourRecursion(n // 4)


# Unit Test: Input: n = 16, Output: True
assert Solution.isPowerOfFour(16) is True

# Unit Test: Input: n = 5, Output: False
assert Solution.isPowerOfFour(5) is False

# Unit Test: Input: n = 1, Output: True
assert Solution.isPowerOfFourBit(1) is True

# Unit Test: Input: n = 0, Output: False
assert Solution.isPowerOfFourRecursion(0) is False

print("All unit tests are passed")
