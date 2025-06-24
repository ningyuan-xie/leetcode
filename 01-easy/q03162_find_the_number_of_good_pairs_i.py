"""3162. Find the Number of Good Pairs I
Link: https://leetcode.com/problems/find-the-number-of-good-pairs-i
Difficulty: Easy
Description: You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively.
You are also given a positive integer k.
A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <=
m - 1).
Return the total number of good pairs."""

from typing import List


class Solution:
    @staticmethod
    def numberOfPairs(nums1: List[int], nums2: List[int], k: int) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n * m), Space Complexity: O(n)."""
        # Initialize a dictionary to count occurrences of each number in nums2
        count = {}
        # Iterate through nums2 and count occurrences
        for num in nums2:
            count[num] = count.get(num, 0) + 1  # {1: 1, 3: 1, 4: 1}

        # Initialize the result variable
        result = 0
        # Iterate through nums1 and check for good pairs
        for num in nums1:
            for key, cnt in count.items():
                if num % (key * k) == 0:
                    result += cnt

        # Return the final result
        return result


# Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1, Output: 5
assert Solution.numberOfPairs([1, 3, 4], [1, 3, 4], 1) == 5

# Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3, Output: 2
assert Solution.numberOfPairs([1, 2, 4, 12], [2, 4], 3) == 2

print("All unit tests are passed.")
