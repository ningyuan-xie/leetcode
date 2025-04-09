"""1189. Maximum Number of Balloons
Link: https://leetcode.com/problems/maximum-number-of-balloons/
Difficulty: Easy
Description: Given a string text, you want to use the characters of text to form as many instances of
the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be
formed."""


class Solution:
    @staticmethod
    def maxNumberOfBalloons(text: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the frequency of each character in text
        freq = {c: 0 for c in "balon"}  # {b: 0, a: 0, l: 0, o: 0, n: 0}

        # Count the frequency of each character in text
        for c in text:
            if c in freq:
                freq[c] += 1

        # Calculate the maximum number of instances of the word "balloon" that can be formed
        return min(freq["b"], freq["a"], freq["l"] // 2, freq["o"] // 2, freq["n"])


# Unit Test: text = "nlaebolko", Output: 1
# Explanation: "balloon" can be formed once using the characters in text.
assert Solution.maxNumberOfBalloons("nlaebolko") == 1

# Unit Test: text = "loonbalxballpoon", Output: 2
# Explanation: "balloon" can be formed twice using the characters in text.
assert Solution.maxNumberOfBalloons("loonbalxballpoon") == 2

# Unit Test: text = "leetcode", Output: 0
# Explanation: "balloon" cannot be formed using the characters in text.
assert Solution.maxNumberOfBalloons("leetcode") == 0

print("All unit tests are passed")
