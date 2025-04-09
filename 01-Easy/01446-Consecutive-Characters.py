"""1446. Consecutive Characters
Link: https://leetcode.com/problems/consecutive-characters/
Difficulty: Easy
Description: The power of the string is the maximum length of a non-empty substring that contains
only one unique character.
Given a string s, return the power of s."""


class Solution:
    @staticmethod
    def maxPower(s: str) -> int:
        """Optimal Solution: Single Pass (Linear Scan): iterate the string just once.
           Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the power and the count of the current character
        power, count = 1, 1

        # Iterate through the string to find the power
        for i in range(1, len(s)):
            # If the current character is the same as the previous character, increment the count
            if s[i] == s[i - 1]:
                count += 1
            # Otherwise, update the power and reset the count
            else:
                power = max(power, count)
                count = 1

        return max(power, count)


# Unit Test: s = "leetcode", Output: 2
assert Solution.maxPower("leetcode") == 2

# Unit Test: s = "abbcccddddeeeeedcba", Output: 5
assert Solution.maxPower("abbcccddddeeeeedcba") == 5

# Unit Test: s = "triplepillooooow", Output: 5
assert Solution.maxPower("triplepillooooow") == 5

# Unit Test: s = "hooraaaaaaaaaaay", Output: 11
assert Solution.maxPower("hooraaaaaaaaaaay") == 11

# Unit Test: s = "tourist", Output: 1
assert Solution.maxPower("tourist") == 1

print("All unit tests are passed.")
