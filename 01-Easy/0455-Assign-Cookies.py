"""455. Assign Cookies
Link: https://leetcode.com/problems/assign-cookies/
Difficulty: Easy
Description: Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child
will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign
the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number."""

from typing import List


class Solution:
    @staticmethod
    def findContentChildren(g: List[int], s: List[int]) -> int:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(nlog(n)), Space Complexity: O(1).
           The solution uses a greedy approach by matching the smallest available cookie to
           the smallest possible greed factor, ensuring each decision maximizes the number
           of content children."""
        # Sort the greed factors and cookie sizes in ascending order
        g.sort()
        s.sort()
        # Initialize two pointers for the greed factors (children) and cookie sizes
        i, j = 0, 0

        # Greedy approach: the algorithm assigns each cookie to the first child it can satisfy,
        # without reconsidering past assignments or backtracking
        while i < len(g) and j < len(s):
            # If the cookie satisfies the greed factor
            if s[j] >= g[i]:
                # Assign the cookie to the child and move to the next child
                i += 1
            # Regardless of whether the current cookie satisfies the current child,
            # the cookie pointer j is incremented to consider the next available cookie
            j += 1
        return i


# Unit Test: Input: g = [1, 2, 3], s = [1, 1], Output: 1
assert Solution.findContentChildren([1, 2, 3], [1, 1]) == 1

# Unit Test: Input: g = [1, 2], s = [1, 2, 3], Output: 2
assert Solution.findContentChildren([1, 2], [1, 2, 3]) == 2

# Unit Test: Input: g = [1, 2, 3], s = [3], Output: 1
assert Solution.findContentChildren([1, 2, 3], [3]) == 1

print("All unit tests are passed")
