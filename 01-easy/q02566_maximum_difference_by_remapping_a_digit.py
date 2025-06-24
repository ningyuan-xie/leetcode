"""2566. Maximum Difference by Remapping a Digit
Link: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
Difficulty: Easy
Description: You are given an integer num. You know that Bob will sneakily remap one of the 10
possible digits (0 to 9) to another digit.
Return the difference between the maximum and minimum values Bob can make by remapping exactly one
digit in num.
Notes:
- When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
- Bob can remap a digit to itself, in which case num does not change.
- Bob can remap different digits for obtaining minimum and maximum values respectively.
- The resulting number after remapping can contain leading zeroes."""


class Solution:
    @staticmethod
    def minMaxDifference(num: int) -> int:
        """Optimal Solution: Integer Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Convert num to string for easy manipulation
        num_str = str(num)  # 11891 -> '11891'

        # Find the maximum value by remapping the 1st non-9 digit to 9
        max_num = num
        for digit in num_str:
            if digit != '9':
                max_num = int(num_str.replace(digit, '9'))
                break

        # Find the minimum value by remapping the 1st digit to 0
        min_num = num
        for digit in num_str:
            min_num = int(num_str.replace(digit, '0'))
            break

        # Return the difference between the maximum and minimum values
        return max_num - min_num


# Input: num = 11891, Output: 99009
assert Solution.minMaxDifference(11891) == 99009

# Input: num = 90, Output: 99
assert Solution.minMaxDifference(90) == 99

print("All unit tests are passed.")
