"""860. Lemonade Change
Link: https://leetcode.com/problems/lemonade-change/
Difficulty: Easy
Description: At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise."""

from typing import List


class Solution:
    @staticmethod
    def lemonadeChange(bills: List[int]) -> bool:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1).
        The solution uses a greedy approach by always prioritizing larger denominations ($10 over $5) when giving change."""
        # Initialize the number of $5 and $10 bills
        five, ten = 0, 0

        # Iterate through the bills
        for bill in bills:
            # If the bill is $5, increment the number of $5 bills
            if bill == 5:
                five += 1
            # If the bill is $10, increment the number of $10 bills and decrement the number of $5 bills
            elif bill == 10:
                ten += 1
                five -= 1
            # If the bill is $20, try to give change with one $10 bill and one $5 bill, otherwise, give change with three $5 bills
            elif bill == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            # If the number of $5 bills is negative, return False
            if five < 0:
                return False

        return True


def unit_tests():
    # Input: [5, 5, 5, 10, 20], Output: True
    assert Solution.lemonadeChange([5, 5, 5, 10, 20]) is True

    # Input: [5, 5, 10], Output: True
    assert Solution.lemonadeChange([5, 5, 10]) is True

    # Input: [10, 10], Output: False
    assert Solution.lemonadeChange([10, 10]) is False

    # Input: [5, 5, 10, 10, 20], Output: False
    assert Solution.lemonadeChange([5, 5, 10, 10, 20]) is False


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")
