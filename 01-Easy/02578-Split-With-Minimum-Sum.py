"""2578. Split With Minimum Sum
Link: https://leetcode.com/problems/split-with-minimum-sum/
Difficulty: Easy
Description: Given a positive integer num, split it into two non-negative integers num1 and num2
such that:
- The concatenation of num1 and num2 is a permutation of num.
-- In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the
number of occurrences of that digit in num.
- num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.
Notes:
- It is guaranteed that num does not contain any leading zeros.
- The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence
of num."""


class Solution:
    @staticmethod
    def splitNum(num: int) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Sort the digits of num in non decreasing order
        digits = sorted(str(num))  # 4325 -> ['2', '3', '4', '5']

        # Assign digits to num1 and num2 alternatively, so that the smaller digits go to higher places
        num1, num2 = "", ""
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                num1 += digit
            else:
                num2 += digit

        # Convert the strings back to integers and return their sum
        return int(num1) + int(num2)


# Unit Test: num = 4325, Output: 59
assert Solution.splitNum(4325) == 59

# Unit Test: num = 687, Output: 75
assert Solution.splitNum(687) == 75

print("All unit tests are passed.")
