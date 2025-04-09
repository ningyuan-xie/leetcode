"""2883. Minimum Hours of Training to Win a Competition
Link: https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/
Difficulty: Easy
Description: You are entering a competition, and are given two positive integers initialEnergy
and initialExperience denoting your initial energy and initial experience respectively.
You are also given two 0-indexed integer arrays energy and experience, both of length n.
You will face n opponents in order. The energy and experience of the ith opponent is denoted by
energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly
greater experience and energy to defeat them and move to the next opponent if available.
Defeating the ith opponent increases your experience by experience[i], but decreases your energy by
energy[i].
Before starting the competition, you can train for some number of hours. After each hour of training,
you can either choose to increase your initial experience by one, or increase your initial energy by one.
Return the minimum number of training hours required to defeat all n opponents."""

from typing import List


class Solution:
    @staticmethod
    def minNumberOfHours(initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        """Optimal Solution: Greedy. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the total training hours needed
        training_hours = 0

        # Greey Approach: Increase minimum training hours needed to defeat each opponent
        for i in range(len(energy)):
            # If initial energy is less than the opponent's energy, we need to train
            if initialEnergy <= energy[i]:
                training_hours += (energy[i] - initialEnergy + 1)  # +1 because strictly greater
                initialEnergy += (energy[i] - initialEnergy + 1)

            # If initial experience is less than or equal to the opponent's experience, we need to train
            if initialExperience <= experience[i]:
                training_hours += (experience[i] - initialExperience + 1)
                initialExperience += (experience[i] - initialExperience + 1)

            # After defeating the opponent, update the initial energy and experience
            initialEnergy -= energy[i]
            initialExperience += experience[i]

        return training_hours


# Unit Test: initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1],
# Output: 8
assert (Solution.minNumberOfHours(5, 3, [1, 4, 3, 2], [2, 6, 3, 1])
        == 8)

# Unit Test: initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]
# Output: 0
assert (Solution.minNumberOfHours(2, 4, [1], [3])
        == 0)

print("All unit tests are passed")
