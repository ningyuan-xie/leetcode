# Link: https://leetcode.com/problems/power-of-two/
# Difficulty: Easy
# Description: Given an integer n, return true if it is a power of two. Otherwise, return false.

class Solution:
    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # If n is a power of 2, then n only has 1 bit = 1, so n & (n - 1) = 0
        # E.g. 4 (100) & 3 (011) = 0, 5 (101) & 4 (100) = 4 (100), 8 (1000) & 7 (0111) = 0
        return n & (n - 1) == 0


# Unit Test: Input: 1
assert Solution.isPowerOfTwo(1) == True

# Unit Test: Input: 16
assert Solution.isPowerOfTwo(16) == True

# Unit Test: Input: 3
assert Solution.isPowerOfTwo(3) == False

# Unit Test: Input: 4
assert Solution.isPowerOfTwo(4) == True

print("All unit tests are passed")
