"""1486. XOR Operation in an Array
Link: https://leetcode.com/problems/xor-operation-in-an-array/
Difficulty: Easy
Description: You are given an integer n and an integer start.
Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums."""


class Solution:
    @staticmethod
    def xorOperation(n: int, start: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the XOR
        xor = 0

        # Iterate through the range of n
        for i in range(n):
            # Update the XOR
            xor ^= start + 2 * i

        # Return the XOR
        return xor


# Unit Test: n = 5, start = 0, Output: 8
# Explanation: 0 ^ 2 = 2, 2 ^ 4 = 6, 6 ^ 6 = 0, 0 ^ 8 = 8
assert Solution.xorOperation(5, 0) == 8

# Unit Test: n = 4, start = 3, Output: 8
# Explanation: 3 ^ 5 = 6, 6 ^ 7 = 1, 1 ^ 9 = 8
assert Solution.xorOperation(4, 3) == 8

# Unit Test: n = 1, start = 7, Output: 7
assert Solution.xorOperation(1, 7) == 7

# Unit Test: n = 10, start = 5, Output: 2
assert Solution.xorOperation(10, 5) == 2

print("All unit tests are passed.")
