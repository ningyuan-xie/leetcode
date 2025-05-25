"""733. Find Smallest Letter Greater Than Target
Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Difficulty: Easy
Description: You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters."""

from typing import List


class Solution:
    @staticmethod
    def next_greatest_letter(letters: List[str], target: str) -> str:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        left, right = 0, len(letters) - 1

        # If the target is greater than the last letter, return the first letter
        if target >= letters[right]:
            return letters[0]

        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return letters[left]


def unit_tests():
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


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
