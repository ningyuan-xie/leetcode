"""1108. Defanging an IP Address
Link: https://leetcode.com/problems/defanging-an-ip-address/
Difficulty: Easy
Description: Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]"."""


class Solution:
    @staticmethod
    def defangIPaddr(address: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)."""
        return address.replace(".", "[.]")


def unit_tests():
    # Input: address = "1.1.1.1", Output: "1[.]1[.]1[.]1"
    assert Solution.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"

    # Input: address = "255.100.50.0", Output: "255[.]100[.]50[.]0"
    assert Solution.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
