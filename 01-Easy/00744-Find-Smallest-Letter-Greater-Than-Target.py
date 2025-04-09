"""733. Find Smallest Letter Greater Than Target
Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Difficulty: Easy
Description: You are given an array of characters letters that is sorted in non-decreasing order,
and a character target. There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters."""

from typing import List


class Solution:
    @staticmethod
    def next_greatest_letter(letters: List[str], target: str) -> str:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Initialize the left and right pointers
        left, right = 0, len(letters) - 1

        # Check if the target is greater than the last letter
        if target >= letters[right]:
            # If so, return the first letter
            return letters[0]

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # Check if the middle letter is greater than the target
            if letters[mid] <= target:
                # If so, move the left pointer to the right
                left = mid + 1
            # Otherwise, move the right pointer to the left
            else:
                right = mid - 1

        # Return the smallest character that is larger than the target
        return letters[left]


# Input: letters = ["c", "f", "j"], target = "a", Output: "c"
assert Solution.next_greatest_letter(["c", "f", "j"], "a") == "c"

# Input: letters = ["c", "f", "j"], target = "c", Output: "f"
assert Solution.next_greatest_letter(["c", "f", "j"], "c") == "f"

# Input: letters = ["c", "f", "j"], target = "d", Output: "f"
assert Solution.next_greatest_letter(["c", "f", "j"], "d") == "f"

# Input: letters = ["c", "f", "j"], target = "g", Output: "j"
assert Solution.next_greatest_letter(["c", "f", "j"], "g") == "j"

# Input: letters = ["c", "f", "j"], target = "k", Output: "c"
assert Solution.next_greatest_letter(["c", "f", "j"], "k") == "c"

print("All unit tests are passed.")
