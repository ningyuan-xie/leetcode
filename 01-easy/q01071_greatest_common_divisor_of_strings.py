"""1071. Greatest Common Divisor of Strings
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
Difficulty: Easy
Description: For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."""


class Solution:
    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        """Optimal Solution: Euclidean Algorithm. Time Complexity: O(n), Space Complexity: O(1)."""
        # If concatenating the two strings in different orders gives different results, no GCD exists
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths of the two strings
        def gcd(a: int, b: int) -> int:
            """Euclidean Algorithm: Recursively find the GCD of two numbers.
            For any two int a and b, the GCD of a and b is the same as the GCD of b and a % b.
            If a number d divides both a and b, then d also divides a % b."""
            while b:
                a, b = b, a % b
            return a

        # Compute the GCD of the lengths and return the prefix of this length
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]


def unit_tests():
    # Input: str1 = "ABCABC", str2 = "ABC", Output: "ABC"
    assert Solution.gcdOfStrings("ABCABC", "ABC") == "ABC"

    # Input: str1 = "ABABAB", str2 = "ABAB", Output: "AB"
    assert Solution.gcdOfStrings("ABABAB", "ABAB") == "AB"

    # Input: str1 = "LEET", str2 = "CODE", Output: ""
    assert Solution.gcdOfStrings("LEET", "CODE") == ""

    # Input: str1 = ""TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", Output: "TAUXX"
    assert Solution.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
