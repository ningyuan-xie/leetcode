"""705. Design HashSet
Link: https://leetcode.com/problems/design-hashset/
Difficulty: Easy
Description: Design a HashSet without using any built-in hash table libraries."""


class MyHashSet:
    """Optimal Solution: List of Buckets. Time Complexity: O(n), Space Complexity: O(n)"""

    def __init__(self):
        """Constructor: Initialize the instance variable"""
        # Initialize the size of the hash set with a prime number to reduce collisions
        self.size = 1001
        # Create a huge list of 1001 empty buckets (lists) to store the keys
        self.buckets = [[] for _ in range(self.size)]

    def __hash_and_bucket(self, key):
        """Helper function to compute the hash value and find the bucket.
           Encapsulation: this is a private method and should not be called outside the class"""
        # Compute the hash value using modulo operation with a prime size
        hash_value = key % self.size
        # Find the bucket at the computed hash value
        return self.buckets[hash_value]

    def add(self, key: int) -> None:
        """Add the key to the hash set"""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # Check if the key is already present: if so, do nothing
        if key not in bucket:
            # If not, add the key to the bucket
            bucket.append(key)

    def remove(self, key: int) -> None:
        """Remove the key from the hash set"""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # Check if the key is present in the bucket: if not, do nothing
        if key in bucket:
            # If present, remove the key
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        """Check if the key is in the hash set"""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # Return True if the key is found in the bucket
        return key in bucket


# Unit Test:
# Input: ["MyHashSet", "add", "add", "contains", "contains",
#         "add", "contains", "remove", "contains"],
# Output: [null, null, null, true, false, null, true, null, false]
hash_set = MyHashSet()  # [[], [], [], ..., []]
hash_set.add(1)  # [[], [1], [], ..., []]
hash_set.add(2)  # [[], [1], [2], ..., []]
assert hash_set.contains(1)
assert not hash_set.contains(3)
hash_set.add(2)
assert hash_set.contains(2)
hash_set.remove(2)
assert not hash_set.contains(2)

print("All unit tests are passed.")
