"""1700. Number of Students Unable to Eat Lunch
Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
Difficulty: Easy
Description: The school cafeteria offers circular and square sandwiches at lunch break, referred to
by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square
or circular sandwiches.
The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are
placed in a stack. At each step:
- If the student at the front of the queue prefers the sandwich on the top of the stack, they will
take it and leave the queue.
- Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable
to eat.
You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the ith
sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the jth
student in the initial queue (j = 0 is the front of the queue). Return the number of students that
are unable to eat."""

from typing import List


class Solution:
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        """Optimal Solution: Preference Counting. Time Complexity: O(n), Space Complexity: O(1).
           Since students will go to the end of the queue if they don't get their preferred sandwich,
           the order of students doesn't matter, but the order of sandwiches does"""
        # Count preferences for each type of sandwich
        count_0 = students.count(0)  # Number of students who prefer type 0
        count_1 = students.count(1)  # Number of students who prefer type 1

        # Iterate through each sandwich in the stack
        for sandwich in sandwiches:
            if sandwich == 0:
                # If sandwich is type 0, check if any student wants it
                if count_0 > 0:
                    count_0 -= 1  # One student who wanted type 0 is satisfied
                else:
                    # No students left who want type 0
                    break
            else:
                # If sandwich is type 1, check if any student wants it
                if count_1 > 0:
                    count_1 -= 1  # One student who wanted type 1 is satisfied
                else:
                    # No students left who want type 1
                    break

        # Students left are those who couldn't get their preferred type
        return count_0 + count_1


# Unit Test: students = [1, 1, 0, 0], sandwiches = [0, 1, 0, 1], Output: 0
assert Solution.count_students([1, 1, 0, 0], [0, 1, 0, 1]) == 0

# Unit Test: students = [1, 1, 1, 0, 0, 1], sandwiches = [1, 0, 0, 0, 1, 1], Output: 3
assert Solution.count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3

print("All unit tests are passed.")
