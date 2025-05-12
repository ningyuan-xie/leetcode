"""599. Minimum Index Sum of Two Lists
Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
Difficulty: Easy
Description: Given two arrays of strings list1 and list2, find the common strings with the least index sum.
A common string is a string that appeared in both list1 and list2.
A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
Return all the common strings with the least index sum. Return the answer in any order."""

from typing import List


class Solution:
    @staticmethod
    def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
        """Optimal Solution: Hash Table. Time Complexity: O(n + m), Space Complexity: O(n)."""
        # Create a dictionary to map strings to their indices in list1
        list1_indices = {string: i for i, string in enumerate(list1)}
        min_sum = float('inf')
        result = []

        # Iterate through list2 and check for common strings
        for j, string in enumerate(list2):
            if string in list1_indices:
                # Calculate the index sum
                current_sum = list1_indices[string] + j
                # Update result based on current sum
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [string]
                elif current_sum == min_sum:
                    result.append(string)
        
        return result


def unit_tests():
    # Input: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"], list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"], Output: ["Shogun"]
    assert Solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"]

    # Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"], Output: ["sad","happy"]
    assert Solution.findRestaurant(["happy","sad","good"], ["sad","happy","good"]) == ["sad","happy"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
