"""944. Delete Columns to Make Sorted
Link: https://leetcode.com/problems/delete-columns-to-make-sorted/
Difficulty: Easy
Description: You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid.
• For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
  abc
  bce
  cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
Return the number of columns that you will delete."""

from typing import List


class Solution:
    @staticmethod
    def minDeletionSize(strs: List[str]) -> int:
        """Optimal Solution: Column-wise Comparison. Time Complexity: O(n * m), Space Complexity: O(1)."""
        delete_count = 0
        
        # Iterate through each column
        for col in zip(*strs):
            # Check if column is sorted by comparing with sorted version
            if list(col) != sorted(col):
                delete_count += 1
                
        return delete_count


def unit_tests():
    # Input: ["cba","daf","ghi"], Output: 1
    assert Solution.minDeletionSize(["cba", "daf", "ghi"]) == 1

    # Input: ["a","b"], Output: 0
    assert Solution.minDeletionSize(["a", "b"]) == 0

    # Input: ["zyx","wvu","tsr"], Output: 3
    assert Solution.minDeletionSize(["zyx", "wvu", "tsr"]) == 3


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
