"""1925. Count Square Sum Triples
Link: https://leetcode.com/problems/count-square-sum-triples/
Difficulty: Easy
Description: A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
Given an integer n, return the number of square triples such that 1 <= a, b, c <= n."""


class Solution:
    @staticmethod
    def countTriples(n: int) -> int:
        """Optimal Solution: Iterative Check. Time Complexity: O(n^2), Space Complexity: O(1)"""
        count = 0

        # Outer Loop: Iterate over c (the hypotenuse)
        for c in range(1, n + 1):
            c_squared = c * c

            # Inner Loop: Iterate over a (one side)
            for a in range(1, c):
                a_squared = a * a
                # Check if b is an integer and within the range
                b_squared = c_squared - a_squared
                b = int(b_squared ** 0.5)
                if b * b == b_squared and 1 <= b <= n:
                    count += 1

        return count


# Unit Test: n = 5, Output: 2
assert Solution.countTriples(5) == 2

# Unit Test: n = 10, Output: 4
assert Solution.countTriples(10) == 4

# Unit Test: n = 1, Output: 0
assert Solution.countTriples(1) == 0

print("All unit tests are passed.")
