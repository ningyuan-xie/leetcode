"""696. Count Binary Substrings
Link: https://leetcode.com/problems/count-binary-substrings/
Difficulty: Easy
Description: Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur."""


class Solution:
    @staticmethod
    def countBinarySubstrings(s: str) -> int:
        """Optimal Solution: Group Counting. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the groups list with the first character
        groups = [1]
        for i in range(1, len(s)):
            # If the current character is different from the previous one, append a new group
            if s[i-1] != s[i]:
                groups.append(1)
            # If the current character is the same as the previous one, increment the last group
            else:
                groups[-1] += 1

        # The number of valid substrings is the minimum of the two group lengths
        count = 0
        for i in range(1, len(groups)):
            count += min(groups[i-1], groups[i])
            
        return count


def unit_tests():
    # Input: s = "00110011", Output: 6
    assert Solution.countBinarySubstrings("00110011") == 6

    # Input: s = "10101", Output: 4
    assert Solution.countBinarySubstrings("10101") == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
