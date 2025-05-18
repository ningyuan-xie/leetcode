"""202. Happy Number
Link: https://leetcode.com/problems/happy-number/
Difficulty: Easy
Description: Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
• Starting with any positive integer, replace the number by the sum of the squares of its digits.
• Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
• Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not."""


class Solution:
    @staticmethod
    def isHappy(n: int) -> bool:
        """Optimal Solution: Set. Time Complexity: O(log(n)), Space Complexity: O(log(n))."""
        seen = set()
        
        # Iterate until n becomes 1 or we find a cycle
        while n != 1 and n not in seen:
            # Add current n to the set of seen numbers
            seen.add(n)
            # Update n to the sum of the squares of its digits
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1


def unit_tests():
    # Input: n = 19, Output: True
    assert Solution.isHappy(19) is True

    # Input: n = 2, Output: False
    assert Solution.isHappy(2) is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
