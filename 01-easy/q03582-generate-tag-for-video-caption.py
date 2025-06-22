"""3582. Generate Tag for Video Caption
Link: https://leetcode.com/problems/generate-tag-for-video-caption
Difficulty: Easy
Description: You are given a string caption representing the caption for a video.
The following actions must be performed in order to generate a valid tag for the video:
1. Combine all words in the string into a single camelCase string prefixed with '#'. A camelCase string is one where the first letter of all words except the first one is capitalized. All characters after the first character in each word must be lowercase.
2. Remove all characters that are not an English letter, except the first '#'.
3. Truncate the result to a maximum of 100 characters.
Return the tag after performing the actions on caption."""

class Solution:
    @staticmethod
    def generateTag(caption: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)."""
        words = caption.split()
        if not words:
            return "#"  # Return "#" if caption is empty

        result = "#"

        # Process first word - all lowercase
        first = ''.join(c.lower() for c in words[0] if c.isalpha())
        if first:
            result += first
            
        # Process remaining words - capitalize first letter, rest lowercase
        for word in words[1:]:
            filtered = ''.join(c for c in word if c.isalpha())
            if filtered:
                result += filtered[0].upper() + filtered[1:].lower()
                
        # Truncate to 100 chars
        return result[:100]


def unit_tests():
    # Input: caption = "Leetcode daily streak achieved", Output: "#leetcodeDailyStreakAchieved"
    assert Solution.generateTag("Leetcode daily streak achieved") == "#leetcodeDailyStreakAchieved"

    # Input: caption = "can I Go There", Output: "#canIGoThere"
    assert Solution.generateTag("can I Go There") == "#canIGoThere"

    # Input: caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", Output: "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    assert Solution.generateTag("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh") == "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"

    # Input: caption = "   ", Output: "#"
    assert Solution.generateTag("   ") == "#"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
