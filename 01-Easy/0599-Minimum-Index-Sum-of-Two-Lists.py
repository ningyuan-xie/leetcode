# Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Difficulty: Easy
# Description: Given two arrays of strings list1 and list2, find the common strings with the
# least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at
# list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

from typing import List


class Solution:
    # Optimal Solution: Hash Map. Time Complexity: O(n + m), Space Complexity: O(n)
    @staticmethod
    def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
        # Initialize a hash map to store the index sum of each common string
        common_index_sum = {}
        # Initialize the minimum index sum
        min_index_sum = float('inf')
        # Initialize the list of common strings with the minimum index sum
        common_strings = []
        # Iterate over each string in list1
        for i, string in enumerate(list1):
            # If the string is in list2
            if string in list2:
                # Calculate the index sum
                index_sum = i + list2.index(string)
                # Update the minimum index sum
                min_index_sum = min(min_index_sum, index_sum)
                # Add the string to the hash map
                common_index_sum[string] = index_sum
        # Iterate over each key-value pair in the hash map
        for key, value in common_index_sum.items():
            # If the index sum is equal to the minimum index sum
            if value == min_index_sum:
                # Add the string to the list of common strings
                common_strings.append(key)
        return common_strings


# Unit Test: Input: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"],
# list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
# Output: ["Shogun"]
assert Solution.findRestaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"]

# Unit Test: Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"],
# Output: ["sad","happy"]
assert Solution.findRestaurant(["happy", "sad", "good"],
                               ["sad", "happy", "good"]) == ["happy", "sad"]

print("All unit tests are passed")
