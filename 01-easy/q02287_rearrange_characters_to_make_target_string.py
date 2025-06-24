"""2287. Rearrange Characters to Make Target String
Link: https://www.leetcode.com/problems/rearrange-characters-to-make-target-string/
Difficulty: Easy
Description: You are given two 0-indexed strings s and target. You can take some letters from s and
rearrange them to form new strings.
Return the maximum number of copies of target that can be formed by taking letters from s and
rearranging them."""


class Solution:
    @staticmethod
    def rearrangeCharacters(s: str, target: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)."""
        # Create two dictionaries to store the frequency of each character in s and target
        frequency, target_frequency = {}, {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        for char in target:
            target_frequency[char] = target_frequency.get(char, 0) + 1

        # Initialize the maximum number of copies of target that can be formed
        max_copies = float("inf")

        # Iterate through the target frequency dictionary
        for (char, count) in target_frequency.items():
            if char not in frequency or frequency[char] < count:
                return 0

            # Calculate the maximum number of copies of target that can be formed
            max_copies = min(max_copies, frequency[char] // count)

        return max_copies


# Input: s = "ilovecodingonleetcode", target = "code", Output: 2
assert Solution.rearrangeCharacters("ilovecodingonleetcode", "code") == 2

# Input: s = "abcba", target = "abc", Output: 1
assert Solution.rearrangeCharacters("abcba", "abc") == 1

# Input: s = "abbaccaddaeea", target = "aaaaa", Output: 1
assert Solution.rearrangeCharacters("abbaccaddaeea", "aaaaa") == 1

print("All unit tests are passed.")
