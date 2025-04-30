"""338. Counting Bits
Link: https://leetcode.com/problems/counting-bits/
Difficulty: Easy
Description: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i."""

from typing import List


class Solution:
    @staticmethod
    def countBits(n: int) -> List[int]:
        """Optimal Solution: Dynamic Programming. Time Complexity: O(n), Space Complexity: O(n)."""
        ans = [0] * (n + 1)

        # Loop through each number from 1 to n
        for i in range(1, n + 1):
            # If i is even, the number of set bits is the same as i // 2
            if i % 2 == 0:
                ans[i] = ans[i // 2]
            # If i is odd, the number of set bits is one more than i // 2
            else:
                ans[i] = ans[i // 2] + 1
        return ans


def unit_tests():
    # Input: n = 2, Output: [0, 1, 1]
    # Explanation: 0 -> 0, 1 -> 1, 2 -> 10
    assert Solution.countBits(2) == [0, 1, 1]

    # Input: n = 5, Output: [0, 1, 1, 2, 1, 2]
    # Explanation: 0 -> 0, 1 -> 1, 2 -> 10, 3 -> 11, 4 -> 100, 5 -> 101
    assert Solution.countBits(5) == [0, 1, 1, 2, 1, 2]

    # Input: n = 10, Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
    # Explanation: 0 -> 0, 1 -> 1, 2 -> 10, 3 -> 11, 4 -> 100, 5 -> 101,
    # 6 -> 110, 7 -> 111, 8 -> 1000, 9 -> 1001, 10 -> 1010
    assert Solution.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
