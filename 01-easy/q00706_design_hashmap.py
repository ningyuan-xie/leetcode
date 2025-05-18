"""706. Design HashMap
Link: https://leetcode.com/problems/design-hashmap/
Difficulty: Easy
Description: Design a HashMap without using any built-in hash table libraries."""


class MyHashMap:
    """Optimal Solution: List of Buckets. Time Complexity: O(n), Space Complexity: O(n).
       Similar to 0705-Design-HashSet.py"""

    def __init__(self):
        """Constructor: Initialize the instance variable"""
        # Initialize the size of the hash set with a prime number to reduce collisions
        self.size = 1001
        # Create a huge list of 1001 empty buckets (lists) to store the key-value pairs
        self.buckets = [[] for _ in range(self.size)]

    def __hash_and_bucket(self, key):
        """Helper function to compute the hash value and find the bucket.
           Encapsulation: this is a private method and should not be called outside the class"""
        # Compute the hash value using modulo operation with a prime size
        hash_value = key % self.size
        # Find the bucket at the computed hash value
        return self.buckets[hash_value]

    def put(self, key: int, value: int) -> None:
        """Put the key-value pair in the hash map"""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # First, check if the key already exists in the bucket
        for i, (k, _) in enumerate(bucket):
            if k == key:
                # If the key exists, update the value at this location i
                bucket[i] = (key, value)
                return

        # If not, add the key-value pair to the bucket
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """Get the value of the key from the hash map"""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # Find the key in the bucket
        for (k, v) in bucket:
            if k == key:
                # If the key is found, return the value
                return v

        # If the key is not found, return -1
        return -1

    def remove(self, key: int) -> None:
        """Remove the key-value pair from the hash map"""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # Check if the key is present in the bucket: if not, do nothing
        for (k, v) in bucket:
            if k == key:
                # If present, remove the key-value pair
                bucket.remove((k, v))


# Input: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
# Output: [null, null, null, 2, -1, null, 2, null, -1]
hash_map = MyHashMap()  # [[], [], [], ..., []]
hash_map.put(1, 1)  # [[], [(1, 1)], [], ..., []]
hash_map.put(2, 2)  # [[], [(1, 1)], [(2, 2)], ..., []]
assert hash_map.get(1) == 1
assert hash_map.get(3) == -1
hash_map.put(2, 1)
assert hash_map.get(2) == 1
hash_map.remove(2)
assert hash_map.get(2) == -1

print("All unit tests are passed.")
