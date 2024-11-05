"""1688. Count of Matches in Tournament
Link: https://leetcode.com/problems/count-of-matches-in-tournament/
Difficulty: Easy
Description: You are given an integer n, the number of teams in a tournament that has strange rules:
- If the current number of teams is even, each team gets paired with another team. A total of
n / 2 matches are played, and n / 2 teams advance to the next round.
- If the current number of teams is odd, one team randomly advances in the tournament, and the
rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to
the next round.
Return the number of matches played in the tournament until a winner is decided."""


class Solution:
    @staticmethod
    def number_of_matches(n: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)"""
        # Rationale: Since only one team remains, all other teams (i.e., n - 1 teams) must be
        # eliminated, and each match eliminates exactly one team.
        return n - 1


# Unit Test: n = 7, Output: 6
assert Solution.number_of_matches(7) == 6

# Unit Test: n = 14, Output: 13
assert Solution.number_of_matches(14) == 13

# Unit Test: n = 9, Output: 8
assert Solution.number_of_matches(9) == 8

print("All unit tests are passed")
