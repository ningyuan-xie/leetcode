"""2119. A Number After a Double Reversal
Link: https://leetcode.com/problems/a-number-after-a-double-reversal
Difficulty: Easy
Description: Reversing an integer means to reverse all its digits.
- For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not
retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2.
Return true if reversed2 equals num. Otherwise return false."""


class Solution:
    @staticmethod
    def doubleReversal(num: int) -> int:
        """Optimal Solution: Reversing the Number.
           Time Complexity: O(n), Space Complexity: O(1)"""

        def reverse(n: int) -> int:
            """Helper function to reverse the number:
               E.g. 1800 -> "1800" -> "0081" -> 81"""
            return int(str(n)[::-1])

        reversed1 = reverse(num)
        reversed2 = reverse(reversed1)
        return reversed2 == num


# Unit Test: Input: num = 526, Output: True
assert Solution.doubleReversal(526) is True

# Unit Test: num = 1800, Output: False
assert Solution.doubleReversal(1800) is False

# Unit Test: num = 0, Output: True
assert Solution.doubleReversal(0) is True

print("All unit tests are passed")
