"""728. Self Dividing Numbers
Link: https://leetcode.com/problems/self-dividing-numbers/
Difficulty: Easy
Description: A self-dividing number is a number that is divisible by every digit it contains.
• For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.
Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive)."""


class Solution:
    @staticmethod
    def selfDividingNumbers(left: int, right: int) -> list[int]:
        """Optimal Solution: Brute Force. Time Complexity: O(n*d), Space Complexity: O(1)."""

        def is_self_dividing(num: int) -> bool:
            """Helper function to check if a number is self-dividing."""
            # Convert number to string and iterate over digits
            str_num = str(num)  
            for digit in str_num:
                if digit == "0" or num % int(digit) != 0:
                    return False
            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]


def unit_tests():
    # Input: left = 1, right = 22, Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert Solution.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    # Input: left = 47, right = 85, Output: [48, 55, 66, 77]
    assert Solution.selfDividingNumbers(47, 85) == [48, 55, 66, 77]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
