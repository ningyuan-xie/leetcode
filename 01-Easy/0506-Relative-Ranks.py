# Link: https://leetcode.com/problems/relative-ranks/
# Difficulty: Easy
# Description: You are given an integer array score of size n, where score[i] is the
# score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# Return an array answer of size n where answer[i] is the ith athlete's rank.

from typing import List


class Solution:
    # Optimal Solution: Sorting. Time Complexity: O(n log n), Space Complexity: O(n)
    @staticmethod
    def findRelativeRanks(score: List[int]) -> List[str]:
        # Sort the scores in descending order
        sorted_score = sorted(score, reverse=True)  # [10, 3, 8, 9, 4] -> [10, 9, 8, 4, 3]
        # Initialize the result array
        result = []
        # Iterate through the scores
        for current_score in score:  # [10, 3, 8, 9, 4]
            # Find the rank of the current score
            rank = sorted_score.index(current_score) + 1  # sorted_score.index(3) = 4 + 1 = 5
            # Assign the rank to the corresponding medal
            if rank == 1:
                result.append("Gold Medal")
            elif rank == 2:
                result.append("Silver Medal")
            elif rank == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(rank))
        return result


# Unit Test: Input: score = [5, 4, 3, 2, 1],
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
assert (Solution.findRelativeRanks([5, 4, 3, 2, 1]) ==
        ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])

# Unit Test: Input: score = [10, 3, 8, 9, 4],
# Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
assert (Solution.findRelativeRanks([10, 3, 8, 9, 4]) ==
        ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"])

# Unit Test: Input: score = [1], Output: ["Gold Medal"]
assert Solution.findRelativeRanks([1]) == ["Gold Medal"]

print("All unit tests are passed")
