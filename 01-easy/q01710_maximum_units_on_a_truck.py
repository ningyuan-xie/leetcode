"""1710. Maximum Units on a Truck
Link: https://leetcode.com/problems/maximum-units-on-a-truck/
Difficulty: Easy
Description: You are assigned to put some amount of boxes onto one truck. You are given a 2D array
boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
- numberOfBoxesi is the number of boxes of type i.
- numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on
the truck. You can choose any boxes to put on the truck as long as the number of boxes does not
exceed truckSize.
Return the maximum total number of units that can be put on the truck."""

from typing import List


class Solution:
    @staticmethod
    def maximum_units(boxTypes: List[List[int]], truckSize: int) -> int:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        # Sort box types by units/box in descending order: higher units/box first
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        # Initialize total units and boxes loaded
        total_units = boxes_loaded = 0

        # Greedy: adding as many of the highest-unit boxes as possible
        for (boxes_num, units) in boxTypes:
            if boxes_loaded + boxes_num <= truckSize:
                # Load all boxes of the current type
                total_units += boxes_num * units
                boxes_loaded += boxes_num
            else:
                # Load remaining boxes of the current type
                remaining_boxes = truckSize - boxes_loaded
                total_units += remaining_boxes * units
                break

        return total_units


# Input: box_types = [[1, 3], [2, 2], [3, 1]], truck_size = 4, Output: 8
assert Solution.maximum_units([[1, 3], [2, 2], [3, 1]], 4) == 8

# Input: box_types = [[5, 10], [2, 5], [4, 7], [3, 9]], truck_size = 10, Output: 91
assert Solution.maximum_units([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91

# Input: box_types = [[1, 1]], truck_size = 1, Output: 1
assert Solution.maximum_units([[1, 1]], 1) == 1

print("All unit tests are passed.")
