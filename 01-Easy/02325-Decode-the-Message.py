"""2325. Decode the Message
Link: https://leetcode.com/problems/decode-the-message/
Difficulty: Easy
Description: You are given the strings key and message, which represent a cipher key and a secret
message, respectively. The steps to decode message are as follows:
1. Use the first appearance of all 26 lowercase English letters in key as the order of the substitution
table.
2. Align the substitution table with the regular English alphabet.
3. Each letter in message is then substituted using the table.
4. Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the
alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd',
'b' -> 'e', 'o' -> 'f').
Return the decoded message."""


class Solution:
    @staticmethod
    def decodeMessage(key: str, message: str) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(1)"""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}

        # Create a mapping from the key to the alphabet
        for i in range(len(key)):
            # If key[i] is not already a key in the dictionary, a new mapping is created
            if key[i] != " " and key[i] not in mapping:
                # Use len(mapping) instead of i because the key may contain spaces
                mapping[key[i]] = alphabet[len(mapping)]

        # Decode the message using the mapping
        decoded_message = ""
        for char in message:
            decoded_message += mapping.get(char, char)
        return decoded_message


# Unit Test: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# Output: "this is a secret"
assert Solution.decodeMessage("the quick brown fox jumps over the lazy dog",
                              "vkbs bs t suepuv") == "this is a secret"

# Unit Test: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# Output: "the five boxing wizards jump quickly"
assert (Solution.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo",
                               "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
        == "the five boxing wizards jump quickly")

print("All unit tests are passed")
