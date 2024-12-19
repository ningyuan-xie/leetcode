"""2129. Capitalize the Title
Link: https://www.leetcode.com/problems/capitalize-the-title
Difficulty: Easy
Description: You are given a string title consisting of one or more words separated by a single space,
where each word consists of English letters. Capitalize the string by changing the capitalization of each \
word such that:
- If the length of the word is 1 or 2 letters, change all letters to lowercase.
- Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title."""


class Solution:
    @staticmethod
    def capitalizeTitle(title: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)"""
        return " ".join([word.capitalize() if len(word) > 2
                         else word.lower()
                         for word in title.split()])


# Unit Test: title = "capiTalIze tHe titLe", Output: "Capitalize The Title"
assert Solution.capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title"

# Unit Test: title = "First leTTeR of EACH Word", Output: "First Letter of Each Word"
assert Solution.capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word"

# Unit Test: title = "i lOve leetcode", Output: "i Love Leetcode"
assert Solution.capitalizeTitle("i lOve leetcode") == "i Love Leetcode"

print("All unit tests are passed")
