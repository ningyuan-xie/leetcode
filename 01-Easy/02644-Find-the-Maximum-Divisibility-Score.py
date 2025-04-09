"""2644. Find the Maximum Divisibility Score
Link: https://leetcode.com/problems/find-the-maximum-divisibility-score/
Difficulty: Easy
Description: You are given two integer arrays nums and divisors.
The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by
divisors[i].
Return the integer divisors[i] with the maximum divisibility score. If multiple integers have the
maximum score, return the smallest one."""

from typing import List


class Solution:
    @staticmethod
    def maxDivScore(nums: List[int], divisors: List[int]) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize variables to track the maximum divisibility score and the corresponding divisor
        max_score = 0
        max_divisor = float('inf')

        # Iterate through each divisor
        for divisor in divisors:
            # Initialize variable to track the divisibility score
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1

            # Update the maximum divisibility score and the corresponding divisor
            if score > max_score or (score == max_score and divisor < max_divisor):
                max_score = score
                max_divisor = divisor

        return max_divisor


# Unit Test: nums = [2,9,15,50], divisors = [5,3,7,2], Output: 2
assert Solution.maxDivScore([2, 9, 15, 50], [5, 3, 7, 2]) == 2

# Unit Test: nums = [4,7,9,3,9], divisors = [5,2,3], Output: 3
assert Solution.maxDivScore([4, 7, 9, 3, 9], [5, 2, 3]) == 3

print("All unit tests are passed.")
