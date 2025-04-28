"""278. First Bad Version
Link: https://leetcode.com/problems/first-bad-version/
Difficulty: Easy
Description: You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API."""


def isBadVersion(version: int) -> bool:
    """ Mock API function: Assume bad version starts from 4"""
    return version >= 4


class Solution:
    @staticmethod
    def firstBadVersion(n: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        # When the loop ends, left is the first bad version
        return left


def unit_tests():
    # Input: n = 5, bad = 4, Output: 4.
    assert Solution.firstBadVersion(5) == 4

    # Input: n = 10, bad = 4, Output: 4.
    assert Solution.firstBadVersion(10) == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
