"""1640. Check Array Formation Through Concatenation
Link: https://leetcode.com/problems/check-array-formation-through-concatenation/
Difficulty: Easy
Description: You are given an array of distinct integers arr and an array of integer arrays pieces,
where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in
pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
Return true if it is possible to form the array arr from pieces. Otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Hash table to store the mapping from the first element of each piece to the piece itself:
        # E.g. [[16, 18, 49]] -> {16: [16, 18, 49]}
        # E.g. [[78], [4, 64], [91]] -> {78: [78], 4: [4, 64], 91: [91]}
        mapping = {piece[0]: piece for piece in pieces}

        # Initialize the result array
        result = []

        # Traverse the array and check if each piece can be formed
        # E.g. arr = [49, 18, 16] -> [] + [] + [16, 18, 49] = [16, 18, 49]
        # E.g. arr = [91, 4, 64, 78] -> [91] + [4, 64] + [] + [78] = [91, 4, 64, 78]
        for num in arr:
            result += mapping.get(num, [])  # .get() returns [] if num is not in the mapping

        return result == arr


# Unit Test: arr = [15, 88], pieces = [[88], [15]], Output: True
assert Solution.canFormArray([15, 88], [[88], [15]]) is True

# Unit Test: arr = [49, 18, 16], pieces = [[16, 18, 49]], Output: False
assert Solution.canFormArray([49, 18, 16], [[16, 18, 49]]) is False

# Unit Test: arr = [91, 4, 64, 78], pieces = [[78], [4, 64], [91]], Output: True
assert Solution.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]) is True

print("All unit tests are passed.")
