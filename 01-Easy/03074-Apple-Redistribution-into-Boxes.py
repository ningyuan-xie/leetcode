"""3074. Apple Redistribution into Boxes
Link: https://leetcode.com/problems/apple-redistribution-into-boxes/
Difficulty: Easy
Description: You are given an array apple of size n and an array capacity of size m.
There are n packs where the ith pack contains apple[i] apples. There are m boxes as well,
and the ith box has a capacity of capacity[i] apples.
Return the minimum number of boxes you need to select to redistribute these n packs of apples
into boxes.
Note that, apples from the same pack can be distributed into different boxes."""

from typing import List


class Solution:
    @staticmethod
    def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
        """Optimal Solution: Sorting. Time Complexity: O(nlogn), Space Complexity: O(1)"""
        # Sort the capacity array in descending order
        capacity.sort(reverse=True)  # [3,9,5,1,9] -> [9,9,5,3,1]

        # Greedily select boxes with the largest capacities to redistribute apples optimally
        boxes = 0
        sum_apples = sum(apple)
        for box in capacity:
            # Base case: If there are no apples left, then break
            if sum_apples <= 0:
                break
            # Fill the current box with apples
            sum_apples -= box
            boxes += 1

        return boxes


# Unit Test: apple = [1,3,2], capacity = [4,3,1,5,2], Output = 2
assert Solution.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]) == 2

# Unit Test: apple = [5,5,5], capacity = [2,4,2,7], Output = 4
assert Solution.minimumBoxes([5, 5, 5], [2, 4, 2, 7]) == 4

# Unit Test: apple = [1,8,3,3,5], capacity = [3,9,5,1,9], Output = 3
assert Solution.minimumBoxes([1, 8, 3, 3, 5], [3, 9, 5, 1, 9]) == 3

# Unit Test: apple = [9,8,8,2,3,1,6], capacity = [10,1,4,10,8,5], Output = 5
assert Solution.minimumBoxes([9, 8, 8, 2, 3, 1, 6], [10, 1, 4, 10, 8, 5]) == 5

print("All unit tests are passed.")
