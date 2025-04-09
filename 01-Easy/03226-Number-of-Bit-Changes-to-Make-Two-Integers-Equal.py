"""3226. Number of Bit Changes to Make Two Integers Equal
Link: https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal
Difficulty: Easy
Description: You are given two positive integers n and k.
You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
Return the number of changes needed to make n equal to k. If it is impossible, return -1."""


class Solution:
    @staticmethod
    def minChanges(n: int, k: int) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(1), Space Complexity: O(1)"""
        count = 0
        for i in range(32):
            # Check if the i-th bit of n and k are different
            n_bit = (n >> i) & 1
            k_bit = (k >> i) & 1

            if n_bit == 1 and k_bit == 0:
                count += 1
            elif n_bit == 0 and k_bit == 1:
                return -1
        return count


# Unit Test: n = 13, k = 4, Output: 2
assert Solution.minChanges(13, 4) == 2

# Unit Test: n = 21, k = 21, Output: 0
assert Solution.minChanges(21, 21) == 0

# Unit Test: n = 14, k = 13, Output: -1
assert Solution.minChanges(14, 13) == -1

print("All unit tests are passed.")
