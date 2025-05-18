"""3370. Smallest Number With All Set Bits
Link: https://leetcode.com/problems/smallest-number-with-all-set-bits/
Difficulty: Easy
Description: You are given a positive number n.
Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits."""


class Solution:
    @staticmethod
    def smallestNumber(n: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(log n), Space Complexity: O(1)."""
        # Find the next power of 2 greater than or equal to n
        power = 1
        while power <= n:
            power *= 2
        return power -1 if power - 1 >= n else power * 2 - 1


def unit_tests():
    # Input: n = 5, Output: 7
    assert Solution.smallestNumber(5) == 7

    # Input: n = 10, Output: 15
    assert Solution.smallestNumber(10) == 15

    # Input: n = 3, Output: 3
    assert Solution.smallestNumber(3) == 3

    # Input: n = 1, Output: 1
    assert Solution.smallestNumber(1) == 1

    # Input: n = 4, Output: 7
    assert Solution.smallestNumber(4) == 7


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
