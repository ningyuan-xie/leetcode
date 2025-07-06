"""3606. Coupon Code Validator
Link: https://leetcode.com/problems/coupon-code-validator/
Difficulty: Easy
Description: You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:
• code[i]: a string representing the coupon identifier.
• businessLine[i]: a string denoting the business category of the coupon.
• isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:
1. code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
2. businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
3. isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category."""

from typing import List

class Solution:
    @staticmethod
    def validateCoupons(code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(n)."""
        valid_business_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        valid_coupons = []

        def is_valid_code(code: str) -> bool:
            """Check if code is non-empty and contains only alphanumeric characters and underscores."""
            return len(code) > 0 and all(c.isalnum() or c == "_" for c in code)
        
        for coupon_code, business_line, is_active in zip(code, businessLine, isActive):
            if is_active and is_valid_code(coupon_code) and business_line in valid_business_lines:
                valid_coupons.append((coupon_code, business_line))
        
        # Sort by business line order, then by code alphabetically
        business_order = ["electronics", "grocery", "pharmacy", "restaurant"]
        valid_coupons.sort(key=lambda x: (business_order.index(x[1]), x[0]))
        
        return [coupon[0] for coupon in valid_coupons]


def unit_tests():
    # Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true], Output: ["PHARMA5","SAVE20"]
    assert Solution.validateCoupons(["SAVE20","","PHARMA5","SAVE@20"], ["restaurant","grocery","pharmacy","restaurant"], [True,True,True,True]) == ["PHARMA5","SAVE20"]

    # Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true], Output: ["ELECTRONICS_50"]
    assert Solution.validateCoupons(["GROCERY15","ELECTRONICS_50","DISCOUNT10"], ["grocery","electronics","invalid"], [False,True,True]) == ["ELECTRONICS_50"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
