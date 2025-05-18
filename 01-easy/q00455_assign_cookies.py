"""455. Assign Cookies
Link: https://leetcode.com/problems/assign-cookies/
Difficulty: Easy
Description: Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number."""

from typing import List


class Solution:
    @staticmethod
    def findContentChildren(g: List[int], s: List[int]) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        # Sort the greed factor and cookie sizes
        g.sort()
        s.sort()

        # Initialize pointers for children and cookies
        child_i, cookie_i = 0, 0
        content_children = 0

        # Iterate through both lists
        while child_i < len(g) and cookie_i < len(s):
            # If the current cookie can satisfy the current child
            if s[cookie_i] >= g[child_i]:
                content_children += 1
                child_i += 1
            # Move to the next cookie
            cookie_i += 1
        return content_children


def unit_tests():
    # Input: g = [1, 2, 3], s = [1, 1], Output: 1
    assert Solution.findContentChildren([1, 2, 3], [1, 1]) == 1

    # Input: g = [1, 2], s = [1, 2, 3], Output: 2
    assert Solution.findContentChildren([1, 2], [1, 2, 3]) == 2

    # Input: g = [1, 2, 3], s = [3], Output: 1
    assert Solution.findContentChildren([1, 2, 3], [3]) == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
