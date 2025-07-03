"""1189. Maximum Number of Balloons
Link: https://leetcode.com/problems/maximum-number-of-balloons/
Difficulty: Easy
Description: Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed."""


class Solution:
    @staticmethod
    def maxNumberOfBalloons(text: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        # Count frequency of each character in text
        freq = {}
        for c in text:
            freq[c] = freq.get(c, 0) + 1
        
        # Calculate max instances of "balloon" based on character requirements
        return min(freq.get("b", 0), freq.get("a", 0), freq.get("l", 0) // 2, freq.get("o", 0) // 2, freq.get("n", 0))


def unit_tests():
    # Input: text = "nlaebolko", Output: 1
    assert Solution.maxNumberOfBalloons("nlaebolko") == 1

    # Input: text = "loonbalxballpoon", Output: 2
    assert Solution.maxNumberOfBalloons("loonbalxballpoon") == 2

    # Input: text = "leetcode", Output: 0
    assert Solution.maxNumberOfBalloons("leetcode") == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
