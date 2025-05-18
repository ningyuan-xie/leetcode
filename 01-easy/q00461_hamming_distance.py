"""461. Hamming Distance
Link: https://leetcode.com/problems/hamming-distance/
Difficulty: Easy
Description: The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them."""


class Solution:
    @staticmethod
    def hammingDistance(x: int, y: int) -> int:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(1), Space Complexity: O(1)."""
        # XOR the two integers to find the positions where the bits differ
        xor_result = x ^ y
        distance = 0

        # Count the number of 1s in the binary representation of the XOR result
        while xor_result:
            # Increment the distance for each 1 found
            distance += xor_result & 1
            # Right shift to check the next bit
            xor_result >>= 1

        return distance


def unit_tests():
    # Input: x = 1, y = 4, Output: 2
    assert Solution.hammingDistance(1, 4) == 2

    # Input: x = 3, y = 1, Output: 1
    assert Solution.hammingDistance(3, 1) == 1

    # Input: x = 0, y = 0, Output: 0
    assert Solution.hammingDistance(0, 0) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
