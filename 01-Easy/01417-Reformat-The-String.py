"""1417. Reformat The String
Link: https://leetcode.com/problems/reformat-the-string/
Difficulty: Easy
Description: You are given an alphanumeric string s. (Alphanumeric string is a string consisting of
lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no
digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string."""


class Solution:
    @staticmethod
    def reformat(s: str) -> str:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize two lists for letters and digits
        letters = [char for char in s if char.isalpha()]
        digits = [char for char in s if char.isdigit()]

        # Check if the difference between the length of two lists is greater than 1
        if abs(len(letters) - len(digits)) > 1:
            return ""

        # Ensure letters list >= digits list, so letters list always go first
        if len(letters) < len(digits):  # E.g. "ab123" -> letters = ["a", "b"], digits = ["1", "2", "3"]
            # Swap the two lists: letters = ["1", "2", "3"], digits = ["a", "b"]
            letters, digits = digits, letters

        # Zip the lists together, and append any remaining character if letters list is longer
        result = [char for pair in zip(letters, digits) for char in pair]
        if len(letters) > len(digits):
            result.append(letters[-1])

        return "".join(result)


# Unit Test: s = "a0b1c2", Output: "a0b1c2"
assert Solution.reformat("a0b1c2") == "a0b1c2"

# Unit Test: s = "leetcode", Output: ""
assert Solution.reformat("leetcode") == ""

# Unit Test: s = "1229857369", Output: ""
assert Solution.reformat("1229857369") == ""

# Unit Test: s = "ab123", Output: "1a2b3"
assert Solution.reformat("ab123") == "1a2b3"

print("All unit tests are passed.")
