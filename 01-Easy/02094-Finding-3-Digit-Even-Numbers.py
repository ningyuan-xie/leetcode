"""2094. Finding 3-Digit Even Numbers
Link: https://leetcode.com/problems/finding-3-digit-even-numbers
Difficulty: Easy
Description: You are given an integer array digits, where each element is a digit. The array may
contain duplicates.
You need to find all the unique integers that follow the given requirements:
- The integer consists of the concatenation of three elements from digits in any arbitrary order.
- The integer does not have leading zeros.
- The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
Return a sorted array of the unique integers."""

from typing import List


class Solution:
    @staticmethod
    def findThreeDigitEvenNumbers(digits: List[int]) -> List[int]:
        """Optimal Solution: Set. Time Complexity: O(n^3), Space Complexity: O(n)"""
        # Use a set to avoid duplicates
        result = set()

        # Loop through all combinations of i, j, k
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i == j:
                    continue  # Skip if the same index is chosen
                for k in range(len(digits)):
                    if k == i or k == j:
                        continue  # Skip if indices overlap

                    # Form the number
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    # Check conditions for a valid 3-digit even number
                    if digits[i] != 0 and digits[k] % 2 == 0:  # First digit non-zero, last digit even
                        result.add(num)

        # Convert the set to a sorted list
        return sorted(result)


# Unit Test: digits = [2,1,3,0], Output: [102,120,130,132,210,230,302,310,312,320]
assert (Solution.findThreeDigitEvenNumbers([2, 1, 3, 0]) ==
        [102, 120, 130, 132, 210, 230, 302, 310, 312, 320])

# Unit Test: digits = [2,2,8,8,2], Output: [222,228,282,288,822,828,882]
assert Solution.findThreeDigitEvenNumbers([2, 2, 8, 8, 2]) == [222, 228, 282, 288, 822, 828, 882]

# Unit Test: digits = [3,7,5], Output: []
assert Solution.findThreeDigitEvenNumbers([3, 7, 5]) == []

print("All unit tests are passed.")
