"""1869. Longer Contiguous Segments of Ones than Zeros
Link: https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
Difficulty: Easy
Description: Given a binary string s, return true if the longest contiguous segment of 1's is
strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.
- For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest
continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a
length 0. The same applies if there is no 1's."""


class Solution:
    @staticmethod
    def checkZeroOnes(s: str) -> bool:
        """Optimal Solution: Keep track of the current count of 1s and 0s and update the max count.
           Time Complexity: O(n), Space Complexity: O(1)."""
        max_ones = max_zeros = 0
        current_ones = current_zeros = 0

        for char in s:
            if char == '1':
                current_ones += 1
                current_zeros = 0
            else:  # char == '0'
                current_zeros += 1
                current_ones = 0

            max_ones = max(max_ones, current_ones)
            max_zeros = max(max_zeros, current_zeros)

        return max_ones > max_zeros


# Unit Test: s = "1101", Output: True
assert Solution.checkZeroOnes("1101") is True

# Unit Test: s = "111000", Output: False
assert Solution.checkZeroOnes("111000") is False

print("All unit tests are passed.")
