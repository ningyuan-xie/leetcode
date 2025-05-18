"""1436. Destination City
Link: https://leetcode.com/problems/destination-city/
Difficulty: Easy
Description: You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists
a direct path going from cityAi to cityBi. Return the destination city, that is, the city without
any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be
exactly one destination city."""

from typing import List


class Solution:
    @staticmethod
    def destCity(paths: List[List[str]]) -> str:
        """Optimal Solution: Hash Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize the hash set to store the cities with outgoing paths
        outgoing = set()

        # Iterate through the paths to store the outgoing cities
        for path in paths:
            outgoing.add(path[0])  # ["cityAi", "cityBi"], cityAi is the outgoing city
            # E.g. outgoing: ["London", "New York", "Lima"]

        # Iterate through the paths to find the destination city
        for path in paths:
            if path[1] not in outgoing:
                return path[1]

        return ""


# Unit Test: paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
# Output: "Sao Paulo"
assert (Solution.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
        == "Sao Paulo")

# Unit Test: paths = [["B", "C"], ["D", "B"], ["C", "A"]], Output: "A"
assert Solution.destCity([["B", "C"], ["D", "B"], ["C", "A"]]) == "A"

# Unit Test: paths = [["A", "Z"]], Output: "Z"
assert Solution.destCity([["A", "Z"]]) == "Z"

# Unit Test: paths = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["E", "F"]], Output: "F"
assert Solution.destCity([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["E", "F"]]) == "F"

print("All unit tests are passed.")
