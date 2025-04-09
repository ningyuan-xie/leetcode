"""1496. Path Crossing
Link: https://leetcode.com/problems/path-crossing/
Difficulty: Easy
Description: Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving
one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane
and walk on the path specified by path.
Return true if the path crosses itself at any point, that is, if at any time you are on a location
you have previously visited. Return false otherwise."""


class Solution:
    @staticmethod
    def isPathCrossing(path: str) -> bool:
        """Optimal Solution: Set Tracking. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the set to store the visited points
        visited = set()
        # Initialize the current point
        x, y = 0, 0
        # Add the current point to the visited set
        visited.add((x, y))

        # Iterate through the path
        for p in path:
            # Update the current point
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1

            # Check if the current point is visited
            if (x, y) in visited:
                # Crossing detected
                return True
            # Add the current point to the visited set
            visited.add((x, y))

        # No crossing detected
        return False


# Unit Test: path = "NES", Output: False
assert Solution.isPathCrossing("NES") == False

# Unit Test: path = "NESWW", Output: True
assert Solution.isPathCrossing("NESWW") == True

# Unit Test: path = "NESW", Output: True
assert Solution.isPathCrossing("NESW") == True

# Unit Test: path = "NESWW", Output: True
assert Solution.isPathCrossing("NESWW") == True

print("All unit tests are passed.")
