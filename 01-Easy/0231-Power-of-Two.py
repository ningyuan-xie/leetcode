# Link: https://leetcode.com/problems/power-of-two/
# Difficulty: Easy
# Description: Given an integer n, return true if it is a power of two. Otherwise, return false.

class Solution:
    # Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)
    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        # The maximum power of 2 that can be stored in a 32-bit integer is 2^30 = 1073741824
        return n > 0 and (2**30) % n == 0

    # Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)
    @staticmethod
    def isPowerOfTwoBit(n: int) -> bool:
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # If n is a power of 2, then n only has 1 bit = 1, so n & (n - 1) = 0
        # E.g. 4 (100) & 3 (011) = 0, 5 (101) & 4 (100) = 4 (100), 8 (1000) & 7 (0111) = 0
        return n & (n - 1) == 0

    # Alternative Solution: Recursion. Time Complexity: O(log(n)), Space Complexity: O(log(n))
    @staticmethod
    def isPowerOfTwoRecursion(n: int) -> bool:
        # Base case: if n is less than or equal to 0, return False
        if n <= 0:
            return False
        # Base case: if n is equal to 1, return True
        if n == 1:
            return True
        # If n is divisible by 2, then recursively check if n // 2 is a power of 2
        return n % 2 == 0 and Solution.isPowerOfTwoRecursion(n // 2)


# Unit Test: Input: 1
assert Solution.isPowerOfTwo(1) == True

# Unit Test: Input: 16
assert Solution.isPowerOfTwo(16) == True

# Unit Test: Input: 3
assert Solution.isPowerOfTwoBit(3) == False

# Unit Test: Input: 4
assert Solution.isPowerOfTwoRecursion(4) == True

print("All unit tests are passed")
