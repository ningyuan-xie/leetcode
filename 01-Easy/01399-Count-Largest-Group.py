"""1399. Count Largest Group
Link: https://leetcode.com/problems/count-largest-group/
Difficulty: Easy
Description: You are given an integer n.
Each number from 1 to n is grouped according to the sum of its digits.
Return the number of groups that have the largest size."""


class Solution:
    @staticmethod
    def countLargestGroup(n: int) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""

        def sum_of_digits(num: int) -> int:
            """Helper function to calculate the sum of digits of a number"""
            return sum(int(digit) for digit in str(num))

        frequency = {}
        for i in range(1, n + 1):
            sum_digits = sum_of_digits(i)
            frequency[sum_digits] = frequency.get(sum_digits, 0) + 1
        max_frequency = max(frequency.values())

        # Count the number of groups that have the largest size
        return sum(1 for value in frequency.values() if value == max_frequency)


# Unit Test: n = 13, Output: 4
assert Solution.countLargestGroup(13) == 4

# Unit Test: n = 2, Output: 2
assert Solution.countLargestGroup(2) == 2

# Unit Test: n = 15, Output: 6
assert Solution.countLargestGroup(15) == 6

# Unit Test: n = 24, Output: 5
assert Solution.countLargestGroup(24) == 5

print("All unit tests are passed")
