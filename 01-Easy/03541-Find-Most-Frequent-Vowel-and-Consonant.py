"""3541. Find Most Frequent Vowel and Consonant.
Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
Difficulty: Easy
Description: You are given a string s consisting of lowercase English letters ('a' to 'z').
Your task is to:
• Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
• Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.
Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
The frequency of a letter x is the number of times it occurs in the string."""

class Solution:
    @staticmethod
    def maxFreqSum(s: str) -> int:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)."""
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_counts = {}
        consonant_counts = {}
        
        for char in s:
            if char in vowels:
                vowel_counts[char] = vowel_counts.get(char, 0) + 1
            else:
                consonant_counts[char] = consonant_counts.get(char, 0) + 1
                
        max_vowel = max(vowel_counts.values()) if vowel_counts else 0
        max_consonant = max(consonant_counts.values()) if consonant_counts else 0
        
        return max_vowel + max_consonant


def unit_tests():
    # Input: s = "successes", Output: 6
    assert Solution.maxFreqSum("successes") == 6
    
    # Input: s = "aeiaeia", Output: 3
    assert Solution.maxFreqSum("aeiaeia") == 3
    

if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
    