"""476. Number Complement
Link: https://leetcode.com/problems/number-complement/
Difficulty: Easy
Description: The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement."""


class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        # Initialize mask to 1
        mask = 1

        # Create a mask with all bits set to 1 for the length of num
        while mask < num:
            mask = (mask << 1) | 1

        # XOR num with the mask to get the complement
        return num ^ mask


def unit_tests():
    # Input: num = 5, Output: 2
    assert Solution.findComplement(5) == 2

    # Input: num = 1, Output: 0
    assert Solution.findComplement(1) == 0

    # Input: num = 7, Output: 0
    assert Solution.findComplement(7) == 0

    # Input: num = 10, Output: 5
    assert Solution.findComplement(10) == 5


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
