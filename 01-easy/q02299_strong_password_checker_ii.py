"""2299. Strong Password Checker II
Link: https://leetcode.com/problems/strong-password-checker-ii/
Difficulty: Easy
Description: A password is said to be strong if it satisfies all the following criteria:
- It has at least 8 characters.
- It contains at least one lowercase letter.
- It contains at least one uppercase letter.
- It contains at least one digit.
- It contains at least one special character. The special characters are the characters in the
following string: "!@#$%^&*()-+".
- It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this
condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false."""


class Solution:
    @staticmethod
    def strongPasswordCheckerII(password: str) -> bool:
        """Optimal Solution: Brute Force. Time Complexity: O(n), Space Complexity: O(1)."""
        if len(password) < 8:
            return False

        has_lower = has_upper = has_digit = has_special = False
        special_chars = set("!@#$%^&*()-+")

        for i, char in enumerate(password):
            if char.islower():
                has_lower = True
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True
            if char in special_chars:
                has_special = True
            if i > 0 and password[i] == password[i - 1]:  # Consecutive identical characters
                return False

        return has_lower and has_upper and has_digit and has_special


# Input: password = "IloveLe3tcode!", Output: True
assert Solution.strongPasswordCheckerII("IloveLe3tcode!") is True

# Input: password = "Me+You--IsMyDream", Output: False
assert Solution.strongPasswordCheckerII("Me+You--IsMyDream") is False

# Input: password = "1aB!", Output: False
assert Solution.strongPasswordCheckerII("1aB!") is False

print("All unit tests are passed.")
