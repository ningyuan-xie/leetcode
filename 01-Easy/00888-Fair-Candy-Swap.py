"""888. Fair Candy Swap
Link: https://leetcode.com/problems/fair-candy-swap/
Difficulty: Easy
Description: Alice and Bob have a different total number of candies. You are given two integer
arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy
that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.
Since they are friends, they would like to exchange one candy box each so that after the exchange,
they both have the same total amount of candy. The total amount of candy a person has is the sum
of the number of candies in each box they have.
Return an integer array answer where answer[0] is the number of candies in the box that Alice
must exchange, and answer[1] is the number of candies in the box that Bob must exchange.
If there are multiple answers, you may return any one of them.
It is guaranteed that at least one answer exists."""

from typing import List


class Solution:
    @staticmethod
    def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """Optimal Solution: Hash Set Lookup and Target Difference Calculation.
           Time Complexity: O(n+m), Space Complexity: O(n)"""
        # Calculate the total number of candies for Alice and Bob
        total_alice, total_bob = sum(aliceSizes), sum(bobSizes)

        # Initialize a hash set to store the candies that Alice has,
        # so that we can look up the candy in O(1) time, instead of O(n) time for list
        alice_candies = set(aliceSizes)

        # Calculate the target difference that Alice and Bob should have
        target_diff = (total_alice - total_bob) // 2

        # Traverse the candies that Bob has
        for bob_candy in bobSizes:
            # Calculate the candy that Alice in theory should give to Bob
            alice_candy = bob_candy + target_diff
            # Check if Alice has the exact candy that she should give to Bob
            if alice_candy in alice_candies:
                return [alice_candy, bob_candy]

        # If there is no answer, return an empty list
        return []


# Input: aliceSizes = [1,1], bobSizes = [2,2], Output: [1,2]
assert Solution.fairCandySwap([1, 1], [2, 2]) == [1, 2]

# Input: aliceSizes = [1,2], bobSizes = [2,3], Output: [1,2]
assert Solution.fairCandySwap([1, 2], [2, 3]) == [1, 2]

# Input: aliceSizes = [2], bobSizes = [1,3], Output: [2,3]
assert Solution.fairCandySwap([2], [1, 3]) == [2, 3]

# Input: aliceSizes = [1,2,5], bobSizes = [2,4], Output: [5,4]
assert Solution.fairCandySwap([1, 2, 5], [2, 4]) == [5, 4]

print("All unit tests are passed.")
