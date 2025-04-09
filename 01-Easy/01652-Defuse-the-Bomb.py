"""1652. Defuse the Bomb
Link: https://leetcode.com/problems/defuse-the-bomb/
Difficulty: Easy
Description: You have a bomb to defuse, and your time is running out! Your informer will provide you
with a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
- If k > 0, replace the ith number with the sum of the next k numbers.
- If k < 0, replace the ith number with the sum of the previous k numbers.
- If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0]
is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!"""

from typing import List


class Solution:
    @staticmethod
    def decrypt(code: List[int], k: int) -> List[int]:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the result array
        n = len(code)
        result = [0] * n

        # Case 1: k = 0
        if k == 0:
            return result

        # Case 2: k > 0
        if k > 0:
            for i in range(n):
                # Add elements from i + 1 to i + k
                for j in range(1, k + 1):
                    # Forward Wrap: [(i + j) % n] move forward and wrap back to the start after
                    # reaching the end. E.g. (0 + 1) % 5 = 1, (4 + 1) % 5 = 0
                    result[i] += code[(i + j) % n]

        # Case 3: k < 0
        else:
            for i in range(n):
                # Add elements from i - 1 to i - k
                for j in range(1, abs(k) + 1):
                    # Backward Wrap: [(i - j) % n] wraps around to the end of the array,
                    # when going backward. E.g. (0 - 1) % 5 = 4, (4 - 1) % 5 = 3
                    result[i] += code[(i - j) % n]

        return result


# Unit Test: code = [5, 7, 1, 4], k = 3, Output: [12, 10, 16, 13]
assert Solution.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]

# Unit Test: code = [1, 2, 3, 4], k = 0, Output: [0, 0, 0, 0]
assert Solution.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]

# Unit Test: code = [2, 4, 9, 3], k = -2, Output: [12, 5, 6, 13]
assert Solution.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]

print("All unit tests are passed")
