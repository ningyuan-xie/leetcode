# Link: https://leetcode.com/problems/first-bad-version/
# Difficulty: Easy
# Description: You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version,
# all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Assume bad version starts from 4
def isBadVersion(version: int) -> bool:
    return version >= 4


class Solution:
    # Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1)
    @staticmethod
    def firstBadVersion(n: int) -> int:
        # Initialize the left and right pointers
        left, right = 1, n
        # Perform binary search to find the first bad version
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        # Can return either left or right since they are equal
        return left


# Unit Test: Input: n = 5, bad = 4, Output: 4
assert Solution.firstBadVersion(5) == 4

# Unit Test: Input: n = 1, bad = 1, Output: 1
assert Solution.firstBadVersion(1) == 1

# Unit Test: Input: n = 10, bad = 4, Output: 4
assert Solution.firstBadVersion(10) == 4

print("All unit tests are passed")
