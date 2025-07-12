"""1313. Decompress Run-Length Encoded List
Link: https://leetcode.com/problems/decompress-run-length-encoded-list/
Difficulty: Easy
Description: We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list."""

from typing import List


class Solution:
    @staticmethod
    def decompressRLElist(nums: List[int]) -> List[int]:
        """Optimal Solution: list.extend() method. Time Complexity: O(n), Space Complexity: O(n)."""
        result = []

        # Traverse the list in pairs
        for i in range(0, len(nums), 2):
            result.extend([nums[i + 1]] * nums[i])

        return result


def unit_tests():
    # Input: nums = [1, 2, 3, 4], Output: [2, 4, 4, 4]
    assert Solution.decompressRLElist([1, 2, 3, 4]) == [2, 4, 4, 4]

    # Input: nums = [1, 1, 2, 3], Output: [1, 3, 3]
    assert Solution.decompressRLElist([1, 1, 2, 3]) == [1, 3, 3]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
