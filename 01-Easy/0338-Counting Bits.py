"""338. Counting Bits
Link: https://leetcode.com/problems/counting-bits/
Difficulty: Easy
Description: Given an integer n, return an array ans of length n + 1
such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i."""

from typing import List


class Solution:
    @staticmethod
    def countBits(n: int) -> List[int]:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(n)
           Using the previous results to calculate the new results:
           1 (0001) -> 1 + dp[n - 1] = 1 + dp[0] = 1;
           2 (0010) -> 1 + dp[n - 2] = 1 + dp[0] = 1; 3 (0011) -> 1 + dp[n - 2] = 1 + dp[1] = 1 + 1 = 2;
           4 (0100) -> 1 + dp[n - 4] = 1 + dp[0] = 1; 6 (0110) -> 1 + dp[n - 4] = 1 + dp[2] = 1 + 1 = 2;
           8 (1000) -> 1 + dp[n - 8] = 1 + dp[0] = 1"""
        # Initialize an array to store the number of 1's in the binary representation
        # of each number from 0 to n
        dp = [0] * (n + 1)
        offset = 1
        # Loop through each number from 1 to n, as 0 has 0 1's
        for i in range(1, n + 1):
            if offset * 2 == i:  # reach the next power of 2, update the offset
                offset = i  # 1, 2, 4, 8, 16, ...
            dp[i] = 1 + dp[i - offset]
        return dp


# Unit Test: Input: n = 2, Output: [0, 1, 1]
# Explanation: 0 -> 0, 1 -> 1, 2 -> 10
assert Solution.countBits(2) == [0, 1, 1]

# Unit Test: Input: n = 5, Output: [0, 1, 1, 2, 1, 2]
# Explanation: 0 -> 0, 1 -> 1, 2 -> 10, 3 -> 11, 4 -> 100, 5 -> 101
assert Solution.countBits(5) == [0, 1, 1, 2, 1, 2]

# Unit Test: Input: n = 10, Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
# Explanation: 0 -> 0, 1 -> 1, 2 -> 10, 3 -> 11, 4 -> 100, 5 -> 101,
# 6 -> 110, 7 -> 111, 8 -> 1000, 9 -> 1001, 10 -> 1010
assert Solution.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

print("All unit tests are passed")
