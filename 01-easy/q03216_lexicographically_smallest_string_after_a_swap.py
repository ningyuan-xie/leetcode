"""3216. Lexicographically Smallest String After a Swap
Link: https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap
Difficulty: Easy
Description: Given a string s containing only digits, return the lexicographically smallest string
that can be obtained after swapping adjacent digits in s with the same parity at most once.
Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2
and 4, have the same parity, while 6 and 9 do not."""

from typing import List


class Solution:
    @staticmethod
    def getSmallestString(s: str) -> str:
        """Optimal Solution: Greedy One-Pass. Time Complexity: O(n), Space Complexity: O(n)."""
        n = len(s)
        chars = list(s)
        best_swap = None
        best_result = s

        for i in range(n - 1):
            if int(chars[i]) % 2 == int(chars[i + 1]) % 2:
                # Try swapping
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
                swapped = ''.join(chars)
                if swapped < best_result:
                    best_result = swapped
                    best_swap = (i, i + 1)
                # Undo the swap
                chars[i], chars[i + 1] = chars[i + 1], chars[i]

        # Apply the best swap if found
        if best_swap:
            i, j = best_swap
            chars[i], chars[j] = chars[j], chars[i]
            return ''.join(chars)
        return s


# Input: s = "45320", Output: "43520"
assert Solution.getSmallestString("45320") == "43520"

# Input: s = "001", Output: "001"
assert Solution.getSmallestString("001") == "001"

# Input: s = "20", Output: "02"
assert Solution.getSmallestString("20") == "02"

print("All unit tests are passed.")
