"""824. Goat Latin
Link: https://leetcode.com/problems/goat-latin/
Difficulty: Easy
Description: You are given a string sentence that consist of words separated by spaces. Each word
consists of lowercase and uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
The rules of Goat Latin are as follows:
If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the
end, then add "ma". For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end,
and so on. Return the final sentence representing the conversion from sentence to Goat Latin."""


class Solution:
    @staticmethod
    def toGoatLatin(sentence: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the vowels set
        vowels = set("aeiouAEIOU")
        # Split the sentence into a list of words
        words = sentence.split()  # E.g. "I speak Goat Latin" -> ["I", "speak", "Goat", "Latin"]

        # Initialize the result list
        result = []
        for i, word in enumerate(words):
            # If the first letter is a vowel, append "ma" to the end of the word
            if word[0] in vowels:
                word += "ma"
            # If the first letter is a consonant, move it to the end and append "ma"
            else:
                word = word[1:] + word[0] + "ma"
            # Append "a" to the end of the word, repeated i + 1 times
            word += "a" * (i + 1)
            result.append(word)

        return " ".join(result)


# Input: sentence = "I speak Goat Latin", Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert Solution.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

# Input: sentence = "The quick brown fox jumped over the lazy dog",
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa
# overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
assert Solution.toGoatLatin("The quick brown fox jumped over the lazy dog") == \
       ("heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa "
        "overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")

print("All unit tests are passed.")
