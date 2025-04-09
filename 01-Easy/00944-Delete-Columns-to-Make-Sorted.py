"""944. Delete Columns to Make Sorted
Link: https://leetcode.com/problems/delete-columns-to-make-sorted/
Difficulty: Easy
Description: You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid.
For example, strs = ["abc", "bce", "cae"] can be arranged as: abc bce cae
You want to delete the columns that are not sorted lexicographically.
In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted,
while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
Return the number of columns that you will delete."""

from typing import List


class Solution:
    @staticmethod
    def minDeletionSize(strs: List[str]) -> int:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n*m), Space Complexity: O(1).
           The solution uses a greedy approach by immediately chooses to delete a column as soon as
           it finds that it's unsorted"""
        # Initialize the count of columns that need to be deleted
        count = 0

        # Greedy approach: check each column individually and make the immediate decision to delete
        for col in range(len(strs[0])):
            # Loop through each row; start from the second row
            for row in range(1, len(strs)):
                # If current row's char < previous row's char, increment the count
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    # Break the inner loop because we don't need to compare the rest of the rows
                    break

        # Return the count of columns that need to be deleted
        return count


# Unit Test: Input: ["cba","daf","ghi"], Output: 1
assert Solution.minDeletionSize(["cba", "daf", "ghi"]) == 1

# Unit Test: Input: ["a","b"], Output: 0
assert Solution.minDeletionSize(["a", "b"]) == 0

# Unit Test: Input: ["zyx","wvu","tsr"], Output: 3
assert Solution.minDeletionSize(["zyx", "wvu", "tsr"]) == 3

print("All unit tests are passed")
