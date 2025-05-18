"""3232. Find if Digit Game Can Be Won
Link: https://leetcode.com/problems/find-if-digit-game-can-be-won
Difficulty: Easy
Description: You are given an array of positive integers nums.
Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers
or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice
wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.
Return true if Alice can win this game, otherwise, return false."""

from typing import List


class Solution:
    @staticmethod
    def canAliceWin(nums: List[int]) -> bool:
        """Optimal Solution: Greedy Approach. Time Complexity: O(n), Space Complexity: O(1)."""
        # Separate single-digit and double-digit numbers
        single_digit_sum = sum(num for num in nums if 1 <= num <= 9)
        double_digit_sum = sum(num for num in nums if 10 <= num <= 99)

        # Calculate total sum of all numbers
        total_sum = sum(nums)

        # Alice's best choice is to pick the larger sum between single-digit and double-digit numbers
        alice_sum = max(single_digit_sum, double_digit_sum)

        # Bob's sum will be the rest of the numbers
        bob_sum = total_sum - alice_sum

        # Alice wins if her sum is greater than Bob's sum
        return alice_sum > bob_sum


# Unit Test: nums = [1,2,3,4,10], Output: False
assert Solution.canAliceWin([1, 2, 3, 4, 10]) is False

# Unit Test: nums = [1,2,3,4,5,14], Output: True
assert Solution.canAliceWin([1, 2, 3, 4, 5, 14]) is True

# Unit Test: nums = [5,5,5,25], Output: True
assert Solution.canAliceWin([5, 5, 5, 25]) is True

print("All unit tests are passed.")
