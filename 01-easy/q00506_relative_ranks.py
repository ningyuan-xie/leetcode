"""506. Relative Ranks
Link: https://leetcode.com/problems/relative-ranks/
Difficulty: Easy
Description: You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
• The 1st place athlete's rank is "Gold Medal".
• The 2nd place athlete's rank is "Silver Medal".
• The 3rd place athlete's rank is "Bronze Medal".
• For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete."""

from typing import List


class Solution:
    @staticmethod
    def findRelativeRanks(score: List[int]) -> List[str]:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(n)."""
        # Create a list of tuples (index, score) and sort it in descending order based on scores
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        # Initialize the result list with empty strings
        result = [""] * len(score)

        # Assign ranks based on the sorted order
        for rank, (index, _) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result


def unit_tests():
    # Input: score = [5, 4, 3, 2, 1], Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert Solution.findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

    # Input: score = [10, 3, 8, 9, 4], Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    assert Solution.findRelativeRanks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]

    # Input: score = [1], Output: ["Gold Medal"]
    assert Solution.findRelativeRanks([1]) == ["Gold Medal"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
