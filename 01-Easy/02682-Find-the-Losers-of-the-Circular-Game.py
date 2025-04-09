"""2682. Find the Losers of the Circular Game
Link: https://leetcode.com/problems/find-the-losers-of-the-circular-game/
Difficulty: Easy
Description: There are n friends that are playing a game. The friends are sitting in a circle and are
numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings
you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the
1st friend.
The rules of the game are as follows:
1st friend receives the ball.
- After that, 1st friend passes it to the friend who is k steps away from them in the clockwise direction.
- After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from
them in the clockwise direction.
- After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from
them in the clockwise direction, and so on and so forth.
In other words, on the ith turn, the friend holding the ball should pass it to the friend who is i * k
steps away from them in the clockwise direction.
The game is finished when some friend receives the ball for the second time.
The losers of the game are friends who did not receive the ball in the entire game.
Given the number of friends, n, and an integer k, return the array answer, which contains the losers
of the game in the ascending order."""

from typing import List


class Solution:
    @staticmethod
    def circularGameLosers(n: int, k: int) -> List[int]:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the list to track the friends
        friends = list(range(1, n + 1))  # n = 5, friends = [1, 2, 3, 4, 5]
        # Initialize the set to track the friends who have received the ball
        friends_set = set()

        # Initialize the index to track the friend who is holding the ball
        index, multiplier = 0, 1
        # Continue the game until the friend receives the ball for the second time
        while friends[index] not in friends_set:
            # Add the friend to the set
            friends_set.add(friends[index])
            # Update the index to the next friend
            index = (index + multiplier * k) % len(friends)
            multiplier += 1

        # The rest of the friends are the losers
        losers = [friend for friend in friends if friend not in friends_set]
        return losers


# Unit Test: n = 5, k = 2, Output: [4,5]
assert Solution.circularGameLosers(5, 2) == [4, 5]

# Unit Test: n = 4, k = 4, Output: [1]
# assert Solution.circularGameLosers(4, 4) == [1]

print("All unit tests are passed.")
