"""1720. Decode XORed Array
Link: https://leetcode.com/problems/decode-xored-array/
Difficulty: Easy
Description: There is a hidden integer array arr that consists of n non-negative integers.
It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i]
XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
You are given the encoded array. You are also given an integer first, that is the first element
of arr, i.e. arr[0].
Return the original array arr. It can be proved that the answer exists and is unique."""

from typing import List


class Solution:
    @staticmethod
    def decode(encoded: List[int], first: int) -> List[int]:
        """Optimal Solution: XOR Properties. Time Complexity: O(n), Space Complexity: O(1).
           XOR reversible property: a ^ b = c -> a ^ c = b and b ^ c = a.
           Since encoded[i] = arr[i] ^ arr[i + 1], arr[i + 1] = arr[i] ^ encoded[i]"""
        # Initialize the decoded array with the first element of the original array
        decoded = [first]

        # Decode the rest of the array
        for i in range(len(encoded)):
            # XOR the current decoded element with the current encoded element
            decoded.append(decoded[-1] ^ encoded[i])

        return decoded


# Unit Test: encoded = [1, 2, 3], first = 1, Output: [1, 0, 2, 1]
assert Solution.decode([1, 2, 3], 1) == [1, 0, 2, 1]

# Unit Test: encoded = [6, 2, 7, 3], first = 4, Output: [4, 2, 0, 7, 4]
assert Solution.decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]

# Unit Test: encoded = [1], first = 1, Output: [1, 0]
assert Solution.decode([1], 1) == [1, 0]

print("All unit tests are passed")
