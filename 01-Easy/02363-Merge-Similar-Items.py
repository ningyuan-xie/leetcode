"""2363. Merge Similar Items
Link: https://leetcode.com/problems/merge-similar-items/
Difficulty: Easy
Description: You are given two 2D integer arrays, items1 and items2, representing two sets of items.
Each array items has the following properties:
- items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight
of the ith item.
- The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights
of all items with value valuei.
Note: ret should be returned in ascending order by value."""

from typing import List


class Solution:
    @staticmethod
    def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Create a hash table to store the sum of weights for each value
        value_weight = {}
        for (value, weight) in items1 + items2:
            value_weight[value] = value_weight.get(value, 0) + weight
        # E.g. items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
        # -> value_weight = {1: 6, 4: 5, 3: 9}

        return sorted([[value, weight]
                       for (value, weight) in value_weight.items()])


# Unit Test: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]], Output: [[1,6],[3,9],[4,5]]
assert (Solution.mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]])
        == [[1, 6], [3, 9], [4, 5]])

# Unit Test: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]], Output: [[1,4],[2,4],[3,4]]
assert (Solution.mergeSimilarItems([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]])
        == [[1, 4], [2, 4], [3, 4]])

print("All unit tests are passed")
