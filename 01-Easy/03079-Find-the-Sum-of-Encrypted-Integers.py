"""3079. Find the Sum of Encrypted Integers
Link: https://leetcode.com/problems/find-the-sum-of-encrypted-integers/
Difficulty: Easy
Description: You are given an integer array nums containing positive integers. We define a
function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x.
For example, encrypt(523) = 555 and encrypt(213) = 333.
Return the sum of encrypted elements."""

from typing import List


class Solution:
    @staticmethod
    def sumOfEncryptedInt(nums: List[int]) -> int:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""

        def encrypt(x: int) -> int:
            """Helper function to encrypt the integer x"""
            return int("".join([max(str(x))] * len(str(x))))

        # Sum the encrypted integers
        return sum(encrypt(x) for x in nums)


# Unit Test: nums = [1,2,3], Output = 6
assert Solution.sumOfEncryptedInt([1, 2, 3]) == 6

# Unit Test: nums = [10,21,31], Output = 66
assert Solution.sumOfEncryptedInt([10, 21, 31]) == 66

print("All unit tests are passed.")
