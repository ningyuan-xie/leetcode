"""728. Self Dividing Numbers
Link: https://leetcode.com/problems/self-dividing-numbers/
Difficulty: Easy
Description: A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.
Given two integers left and right, return a list of all the self-dividing numbers in the
range [left, right]"""


class Solution:
    @staticmethod
    def selfDividingNumbers(left: int, right: int):
        """Optimal Solution: Brute Force. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the result list
        result = []
        # Iterate through the range
        for num in range(left, right + 1):
            # Check if the number is self-dividing
            if Solution.is_self_dividing(num):
                # If so, add it to the result list
                result.append(num)

        # Return the result list
        return result

    @staticmethod
    def is_self_dividing(num: int) -> bool:
        """Helper function to check if a number is self-dividing"""
        # Initialize the original number
        original_num = num
        # Iterate through the digits of the number
        while num > 0:
            # Get the last digit
            digit = num % 10
            # Check if the digit is 0 or if the number is not divisible by the digit
            if digit == 0 or original_num % digit != 0:
                # If so, return False
                return False
            # Update the number by removing the last digit
            num //= 10
        # If all digits are self-dividing, return True
        return True


# Input: left = 1, right = 22, Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert Solution.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# Input: left = 47, right = 85, Output: [48, 55, 66, 77]
assert Solution.selfDividingNumbers(47, 85) == [48, 55, 66, 77]

print("All unit tests are passed.")
