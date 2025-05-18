"""2496. Maximum Value of a String in an Array
Link: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
Difficulty: Easy
Description: The value of an alphanumeric string can be defined as:
- The numeric representation of the string in base 10, if it comprises of digits only.
- The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs."""


class Solution:
    @staticmethod
    def maximumValue(strs: list[str]) -> int:
        """Optimal Solution: Compare and Update. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the maximum value to 0
        max_value = 0

        # Iterate through each word in the list
        for word in strs:
            # Check if the word is numeric
            if word.isnumeric():
                # Update the maximum value if the current word's integer value is greater
                max_value = max(max_value, int(word))
            else:
                # Update the maximum value if the current word's length is greater
                max_value = max(max_value, len(word))

        return max_value


# Unit Test: words = ["alic3", "bob", "3", "4", "00000"], Output: 5
assert Solution.maximumValue(["alic3", "bob", "3", "4", "00000"]) == 5

# Unit Test: words = ["1", "01", "001", "0001"], Output: 1
assert Solution.maximumValue(["1", "01", "001", "0001"]) == 1

print("All unit tests are passed.")
