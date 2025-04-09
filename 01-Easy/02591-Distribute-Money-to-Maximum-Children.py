"""2591. Distribute Money to Maximum Children
Link: https://leetcode.com/problems/distribute-money-to-maximum-children/
Difficulty: Easy
Description: You are given an integer money denoting the amount of money (in dollars) that you have and
another integer children denoting the number of children that you must distribute the money to.
You have to distribute the money according to the following rules:
- All money must be distributed.
- Everyone must receive at least 1 dollar.
- Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money
according to the aforementioned rules. If there is no way to distribute the money, return -1."""


class Solution:
    @staticmethod
    def distMoney(money: int, children: int) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(1), Space Complexity: O(1).
           Greedy: We try to maximize the number of children who receive exactly 8 dollars first"""
        # Base case, impossible condition
        if money < children:
            return -1  # Not enough money to give at least $1 per child

        # Calculate maximum children that can receive exactly 8 dollars
        max_eights = min((money - children) // 7, children)  # Each child already gets 1 dollar

        # Compute remaining money and remaining children
        remaining_money = money - (max_eights * 8)  # Money left after distributing `max_eights` 8s
        remaining_children = children - max_eights  # Children left to receive money

        # Handle edge case where remaining money is exactly 4
        if remaining_money == 4 and remaining_children == 1:
            max_eights -= 1  # Avoid giving exactly 4 dollars to a child

        # Handle edge case where there is no children left but there is remaining money
        if remaining_children == 0 and remaining_money > 0:
            max_eights -= 1  # Avoid wasted money when no children left

        return max_eights


# Unit Test: money = 20, children = 3, Output: 1
assert Solution.distMoney(20, 3) == 1

# Unit Test: money = 16, children = 2, Output: 2
assert Solution.distMoney(16, 2) == 2

# United Test: money = 17, children = 2, Output: 1
assert Solution.distMoney(17, 2) == 1

# Unit Test: money = 8, children = 2, Output: 0
assert Solution.distMoney(8, 2) == 0

# Unit Test: money = 23, children = 2, Output: 1
assert Solution.distMoney(23, 2) == 1

print("All unit tests are passed")
