"""1952. Three Divisors
Link: https://leetcode.com/problems/three-divisors/
Difficulty: Easy
Description: Given an integer n, return true if n has exactly three positive divisors. Otherwise,
return false.
An integer m is a divisor of n if there exists an integer k such that n = k * m."""


class Solution:
    @staticmethod
    def isThree(n: int) -> bool:
        """Optimal Solution: Math. Time Complexity: O(sqrt(n)), Space Complexity: O(1)."""
        # Count the number of divisors
        count = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                count += 1
                # Also count in the other side of the divisor
                if i != n // i:
                    count += 1

        return count == 3


# Unit Test: n = 2, Output: False
assert Solution.isThree(2) is False

# Unit Test: n = 4, Output: True
assert Solution.isThree(4) is True

# Unit Test: n = 5, Output: False
assert Solution.isThree(5) is False

print("All unit tests are passed.")
