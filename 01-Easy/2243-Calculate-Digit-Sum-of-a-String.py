"""2243. Calculate Digit Sum of a String
Link: https://leetcode.com/problems/calculate-digit-sum-of-a-string/
Difficulty: Easy
Description: You are given a string s consisting of digits and an integer k.
A round can be completed if the length of s is greater than k. In one round, do the following:
1. Divide s into consecutive groups of size k such that the first k characters are in the first
group, the next k characters are in the second group, and so on. Note that the size of the last
group can be smaller than k.
2. Replace each group of s with a string representing the sum of all its digits. For example,
"346" is replaced with "13" because 3 + 4 + 6 = 13.
3. Merge consecutive groups together to form a new string. If the length of the string is greater
than k, repeat from step 1.
Return s after all rounds have been completed."""

from typing import List


class Solution:
    @staticmethod
    def digitSum(s: str, k: int) -> str:
        """Optimal Solution: While Loop. Time Complexity: O(n), Space Complexity: O(1)"""
        while len(s) > k:
            # For each round, initialize a new string to store the results
            new_s = []
            for i in range(0, len(s), k):
                # Extract the group of digits
                group = s[i:i + k]  # E.g. "111", "112", "222", "23"
                # Compute the sum of digits in the group
                group_sum = sum(map(int, group))  # E.g. 3, 4, 6, 5
                # Append the result to the new string
                new_s.append(str(group_sum))  # E.g. "3", "4", "6", "5"
            # Update the string with the concatenated results
            s = "".join(new_s)  # E.g. "3465"

        return s


# Unit Test: s = "11111222223", k = 3, Output: "135"
assert Solution.digitSum("11111222223", 3) == "135"

# Unit Test: s = "00000000", k = 3, Output: "000"
assert Solution.digitSum("00000000", 3) == "000"

print("All unit tests are passed")
