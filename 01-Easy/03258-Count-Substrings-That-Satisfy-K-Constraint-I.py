"""3258. Count Substrings That Satisfy K Constraint I
Link: https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/
Difficulty: Easy
Description: You are given a binary string s and an integer k.
A binary string satisfies the k-constraint if either of the following conditions holds:
- The number of 0's in the string is at most k.
- The number of 1's in the string is at most k.
Return an integer denoting the number of substrings of s that satisfy the k-constraint."""


class Solution:
    @staticmethod
    def countKConstraintSubstrings(s: str, k: int) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(s)
        count = 0
        left = 0
        zero_count, one_count = 0, 0

        # Iterate through the string with a sliding window
        for right in range(n):
            if s[right] == '0':
                zero_count += 1
            else:
                one_count += 1

            # Shrink the window from left until the k-constraint is satisfied
            while zero_count > k and one_count > k:
                if s[left] == '0':
                    zero_count -= 1
                else:
                    one_count -= 1
                left += 1

            # Count the number of valid substrings ending at current right index
            count += right - left + 1

        return count
    

# Unit Test: s = "10101", k = 1, Output: 12
assert Solution.countKConstraintSubstrings("10101", 1) == 12

# Unit Test: s = "1010101", k = 2, Output: 25
assert Solution.countKConstraintSubstrings("1010101", 2) == 25

# Unit Test: s = "11111", k = 1, Output: 15
assert Solution.countKConstraintSubstrings("11111", 1) == 15

print("All unit tests are passed.")
