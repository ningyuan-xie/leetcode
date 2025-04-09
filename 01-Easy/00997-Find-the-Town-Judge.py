"""997. Find the Town Judge
Link: https://leetcode.com/problems/find-the-town-judge/
Difficulty: Easy
Description: In a town, there are n people labeled from 1 to n. There is a rumor that one of these
people is secretly the town judge. If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai
trusts the person labeled bi. If a trust relationship does not exist in trust array, then such
a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified,
or return -1 otherwise."""

from typing import List


class Solution:
    @staticmethod
    def findJudge(n: int, trust: List[List[int]]) -> int:
        """Optimal Solution: Indegree and Outdegree.
           Time Complexity: O(n), Space Complexity: O(n)"""
        # indegree: how many people trust the person; if n - 1, then everyone trusts the person
        # outdegree: how many people the person trusts; if 0, then the person trusts nobody
        indegree, outdegree = [0] * (n + 1), [0] * (n + 1)  # n + 1 as people are labeled from 1 to n

        # Loop through the trust array to update the indegree and outdegree arrays
        for (a, b) in trust:  # E.g. trust = [[1, 3], [2, 3]]
            indegree[b] += 1  # indegree = [0, 0, 0, 2]
            outdegree[a] += 1  # outdegree = [0, 1, 1, 0]

        # Loop through the indegree and outdegree arrays to find the town judge
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i

        return -1


# Unit Test: Input: n = 2, trust = [[1,2]], Output: 2
assert Solution.findJudge(2, [[1, 2]]) == 2

# Unit Test: Input: n = 3, trust = [[1,3],[2,3]], Output: 3
assert Solution.findJudge(3, [[1, 3], [2, 3]]) == 3

# Unit Test: Input: n = 3, trust = [[1,3],[2,3],[3,1]], Output: -1
assert Solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1

# Unit Test: Input: n = 3, trust = [[1,2],[2,3]], Output: -1
assert Solution.findJudge(3, [[1, 2], [2, 3]]) == -1

print("All unit tests are passed")
