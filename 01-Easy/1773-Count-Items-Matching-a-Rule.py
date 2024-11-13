"""1773. Count Items Matching a Rule
Link: https://leetcode.com/problems/count-items-matching-a-rule/
Difficulty: Easy
Description: You are given an array items, where each items[i] = [typei, colori, namei] describes
the type, color, and name of the ith item. You are also given a rule represented by two strings,
ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
- ruleKey == "type" and ruleValue == typei.
- ruleKey == "color" and ruleValue == colori.
- ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule."""

from typing import List


class Solution:
    @staticmethod
    def count_matches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """Optimal Solution: One Pass. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the count of items that match the rule
        count = 0

        # Check each item to see if it matches the rule
        for item in items:
            # Check the rule based on the rule key
            if ruleKey == "type" and item[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and item[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and item[2] == ruleValue:
                count += 1

        return count


# Unit Test: items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
#                     ["phone", "gold", "iphone"]], rule_key = "color", rule_value = "silver",
# Output: 1
assert Solution.count_matches([["phone", "blue", "pixel"],
                               ["computer", "silver", "lenovo"],
                               ["phone", "gold", "iphone"]], "color", "silver") == 1

# Unit Test: items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"],
#                     ["phone", "gold", "iphone"]], ruleKey = "type", ruleValue = "phone",
# Output: 2
assert Solution.count_matches([["phone", "blue", "pixel"],
                               ["computer", "silver", "phone"],
                               ["phone", "gold", "iphone"]], "type", "phone") == 2

print("All unit tests are passed")
