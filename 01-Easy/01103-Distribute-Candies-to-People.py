"""1103. Distribute Candies to People
Link: https://leetcode.com/problems/distribute-candies-to-people/
Difficulty: Easy
Description: We distribute some number of candies, to a row of n = num_people people in the following
way:
We then give 1 candy to the first person, 2 candies to the second person, and so on until we give
n candies to the last person.
Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to
the second person, and so on until we give 2 * n candies to the last person.
This process repeats (with us giving one more candy each time, and moving to the start of the row
after we reach the end) until we run out of candies.  The last person will receive all of our
remaining candies (not necessarily one more than the previous gift).
Return an array (of length num_people and sum candies) that represents the final distribution
of candies."""

from typing import List


class Solution:
    @staticmethod
    def distributeCandies(candies: int, num_people: int) -> List[int]:
        """Optimal Solution: Step-based Distribution.
           Time Complexity: O(sqrt(candies)), Space Complexity: O(n)"""
        # Initialize an array to store the candies for each person
        distribution = [0] * num_people
        # This is the step count, representing the current distribution
        step = 0

        while candies > 0:
            # Find the index of the person to give candies to in this step
            person = step % num_people

            # Determine how many candies to give in this step: either step + 1, or remaining candies
            current_candies = min(step + 1, candies)

            # Distribute the candies to the current person
            distribution[person] += current_candies

            # Subtract the distributed candies from the total number of candies
            candies -= current_candies

            # Move to the next step
            step += 1

        return distribution


# Unit Test: candies = 7, num_people = 4, Output: [1, 2, 3, 1]
assert Solution.distributeCandies(7, 4) == [1, 2, 3, 1]

# Unit Test: candies = 10, num_people = 3, Output: [5, 2, 3]
assert Solution.distributeCandies(10, 3) == [5, 2, 3]

# Unit Test: candies = 60, num_people = 4, Output: [15, 18, 15, 12]
assert Solution.distributeCandies(60, 4) == [15, 18, 15, 12]

print("All unit tests are passed")
