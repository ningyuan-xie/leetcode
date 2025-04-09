"""942. DI String Match
Link: https://leetcode.com/problems/di-string-match/
Difficulty: Easy
Description: A permutation perm of n + 1 integers of all the integers in the range [0, n] can be
represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it.
If there are multiple valid permutations perm, return any of them."""

from typing import List


class Solution:
    @staticmethod
    def diStringMatch(s: str) -> List[int]:
        """Optimal Solution: Greedy Algorithm and Two Pointers.
           Time Complexity: O(n), Space Complexity: O(n).
           The solution uses a greedy approach by always prioritizing the left pointer when
           the character is 'I' and the right pointer when the character is 'D'"""
        # Initialize left/right as min/max available numbers that can be used in the permutation
        left, right, perm = 0, len(s), []

        # Greedy approach: ensure that the permutation respects the required order
        for char in s:
            # If the char is 'I', add the smallest number available and increment the left pointer
            if char == 'I':
                perm.append(left)
                left += 1
            # If the char is 'D', add the largest number available and decrement the right pointer
            else:
                perm.append(right)
                right -= 1

        # After looping through all the chars, left and right converge to the same remaining number
        perm.append(left)

        # Return the result
        return perm


# Unit Test: Input: "IDID", Output: [0,4,1,3,2]
assert Solution.diStringMatch("IDID") == [0, 4, 1, 3, 2]

# Unit Test: Input: "III", Output: [0,1,2,3]
assert Solution.diStringMatch("III") == [0, 1, 2, 3]

# Unit Test: Input: "DDI", Output: [3,2,0,1]
assert Solution.diStringMatch("DDI") == [3, 2, 0, 1]

print("All unit tests are passed")
