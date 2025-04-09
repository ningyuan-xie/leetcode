"""2231. 2231. Largest Number After Digit Swaps by Parity
Link: https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
Difficulty: Easy
Description: You are given a positive integer num. You may swap any two digits of num that have
the same parity (i.e. both odd digits or both even digits).
Return the largest possible value of num after any number of swaps."""

from typing import List


class Solution:
    @staticmethod
    def largestInteger(num: int) -> int:
        """Optimal Solution: Parity Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(n)"""
        # Convert the number to a list of digits
        digits = list(map(int, str(num)))  # E.g. 1234 -> [1, 2, 3, 4]

        # Separate digits into odd and even
        odd_digits = sorted([d for d in digits if d % 2 != 0], reverse=True)  # [3, 1]
        even_digits = sorted([d for d in digits if d % 2 == 0], reverse=True)  # [4, 2]

        # Rebuild the largest number by parity
        result = []
        for d in digits:
            if d % 2 == 0:
                result.append(even_digits.pop(0))  # Take the largest available even
            else:
                result.append(odd_digits.pop(0))  # Take the largest available odd

        # Convert the result list back to an integer
        return int("".join(map(str, result)))


# Unit Test: num = 1234, Output: 3412
assert Solution.largestInteger(1234) == 3412

# Unit Test: num = 65875, Output: 87655
assert Solution.largestInteger(65875) == 87655

print("All unit tests are passed")
