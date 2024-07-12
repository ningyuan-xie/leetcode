# Link: https://leetcode.com/problems/plus-one/
# Difficulty: Easy
# Description: Given a non-empty array of decimal digits representing a non-negative integer,
# increment one to the integer.

from typing import List


class Solution:
    # Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        # Loop through the index of the numbers in the list in reverse order from right to left
        # -1: the stopping condition so loop will stop before -1 (at 0)
        for i in range(len(digits) - 1, -1, -1):  # E.g. [1, 2, 3] -> 3, 2, 1
            # If the number is less than 9, add 1 to the number and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the number is 9, set the number to 0
            digits[i] = 0  # E.g. [9, 9, 9] -> [9, 9, 0] -> [9, 0, 0] -> [0, 0, 0]
        # If all the numbers were 9, add 1 to the front of the list
        return [1] + digits  # E.g. [9, 9, 9] -> [0, 0, 0] -> [1, 0, 0, 0]


# Unit Test: Input: digits = [1, 2, 3], Output: [1, 2, 4]
assert Solution.plusOne([1, 2, 3]) == [1, 2, 4]

# Unit Test: Input: digits = [4, 3, 2, 1], Output: [4, 3, 2, 2]
assert Solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

# Unit Test: Input: digits = [0], Output: [1]
assert Solution.plusOne([0]) == [1]

print("All unit tests are passed")
