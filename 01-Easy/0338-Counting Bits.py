# Link: https://leetcode.com/problems/counting-bits/
# Difficulty: Easy
# Description: Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

from typing import List


class Solution:
    # Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def countBits(n: int) -> List[int]:
        # Initialize an array to store the number of 1's in the binary representation
        # of each number from 0 to n
        ans = [0] * (n + 1)

        # Loop through each number from 1 to n
        for i in range(1, n + 1):
            # The number of 1's in the binary representation of i is equal to
            # the number of 1's in the binary representation of i // 2
            # plus 1 if i is odd, or 0 if i is even
            ans[i] = ans[i // 2] + (i % 2)

        return ans


# Unit Test: Input: n = 2, Output: [0, 1, 1]
assert Solution.countBits(2) == [0, 1, 1]

# Unit Test: Input: n = 5, Output: [0, 1, 1, 2, 1, 2]
assert Solution.countBits(5) == [0, 1, 1, 2, 1, 2]

# Unit Test: Input: n = 10, Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
assert Solution.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

print("All unit tests are passed")
