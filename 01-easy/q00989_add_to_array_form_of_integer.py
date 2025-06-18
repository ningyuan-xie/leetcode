"""989. Add to Array-Form of Integer
Link: https://leetcode.com/problems/add-to-array-form-of-integer/
Difficulty: Easy
Description: The array-form of an integer num is an array representing its digits in left to right order.
• For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k."""

from typing import List


class Solution:
    @staticmethod
    def addToArrayForm(num: List[int], k: int) -> List[int]:
        """Optimal Solution: Math. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 415. Add-Strings and 504. Base-7."""
        num_len, carry = len(num), k

        # Loop through the array in reverse order
        for i in range(num_len - 1, -1, -1):
            total = num[i] + carry
            remainder, carry = total % 10, total // 10
            num[i] = remainder

        # If there's any carry left, handle it by adding digits to the front (left) of the array
        while carry > 0:
            remainder = carry % 10
            # Update the current digit with the remainder
            num.insert(0, remainder)
            # Update the carry by moving to the left digit
            carry //= 10

        return num


def unit_tests():
    # Input: A = [1,2,0,0], K = 34, Output: [1,2,3,4]
    assert Solution.addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]

    # Input: A = [2,7,4], K = 181, Output: [4,5,5]
    assert Solution.addToArrayForm([2, 7, 4], 181) == [4, 5, 5]

    # Input: A = [2,1,5], K = 806, Output: [1,0,2,1]
    assert Solution.addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
