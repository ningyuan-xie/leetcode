"""1370. Increasing Decreasing String
Link: https://leetcode.com/problems/increasing-decreasing-string/
Difficulty: Easy
Description: You are given a string s. Reorder the string using the following algorithm::
1. Remove the smallest character from s and append it to the result.
2. Remove the smallest character from s that is greater than the last appended character,
and append it to the result.
3. Repeat step 2 until no more characters can be removed.
4. Remove the largest character from s and append it to the result.
5. Remove the largest character from s that is smaller than the last appended character,
and append it to the result.
6. Repeat step 5 until no more characters can be removed.
7. Repeat steps 1 through 6 until all characters from s have been removed.
If the smallest or largest character appears more than once, you may choose any occurrence to append
to the result.
Return the resulting string after reordering s using this algorithm."""


class Solution:
    @staticmethod
    def sortString(s: str) -> str:
        """Optimal Solution: Counting Sort. Time Complexity: O(n), Space Complexity: O(n).
           Similar to 1051-Height-Checker.py"""
        count = [0] * 26

        # Count the frequency of each character in the string
        # E.g. "aaaabbbbcccc" -> [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, ..., 0]
        for char in s:
            count[ord(char) - ord('a')] += 1  # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25

        result = []
        n = len(s)

        while n > 0:
            # Increasing: Append the smallest character from s to the result
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))  # i: 0 -> 'a', 1 -> 'b', ..., 25 -> 'z'
                    count[i] -= 1
                    n -= 1

            # Decreasing: Append the largest character from s to the result
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
                    n -= 1

        return "".join(result)


# Input: s = "aaaabbbbcccc", Output: "abccbaabccba"
assert Solution.sortString("aaaabbbbcccc") == "abccbaabccba"

# Input: s = "rat", Output: "art"
assert Solution.sortString("rat") == "art"

# Input: s = "leetcode", Output: "cdelotee"
assert Solution.sortString("leetcode") == "cdelotee"

# Input: s = "ggggggg", Output: "ggggggg"
assert Solution.sortString("ggggggg") == "ggggggg"

# Input: s = "spo", Output: "ops"
assert Solution.sortString("spo") == "ops"

print("All unit tests are passed.")
