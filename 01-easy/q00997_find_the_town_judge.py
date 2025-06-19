"""997. Find the Town Judge
Link: https://leetcode.com/problems/find-the-town-judge/
Difficulty: Easy
Description: In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise."""

from typing import List


class Solution:
    @staticmethod
    def findJudge(n: int, trust: List[List[int]]) -> int:
        """Optimal Solution: Graph Theory - Net Trust Score. Time Complexity: O(n), Space Complexity: O(n)."""
        trust_score = [0] * (n + 1)

        # Calculate net trust score for each person
        for a, b in trust:
            trust_score[a] -= 1  # Person a trusts someone (negative score)
            trust_score[b] += 1  # Person b is trusted (positive score)

        # Find person with score n-1 (if any)
        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i

        return -1


def unit_tests():
    # Input: n = 2, trust = [[1,2]], Output: 2
    assert Solution.findJudge(2, [[1, 2]]) == 2

    # Input: n = 3, trust = [[1,3],[2,3]], Output: 3
    assert Solution.findJudge(3, [[1, 3], [2, 3]]) == 3

    # Input: n = 3, trust = [[1,3],[2,3],[3,1]], Output: -1
    assert Solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1

    # Input: n = 3, trust = [[1,2],[2,3]], Output: -1
    assert Solution.findJudge(3, [[1, 2], [2, 3]]) == -1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
