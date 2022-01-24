# We define the usage of capitals in a word to be right when one of the following cases holds:
#   - All letters in this word are capitals, like "USA".
#   - All letters in this word are not capitals, like "leetcode".
#   - Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        
        def capital(letter):
            if letter >= 'A' and letter <= 'Z':
                return True
            else:
                return False
            
        if not capital(word[0]):
            for letter in word[1:]:
                if capital(letter):
                    return False
            return True
        else:
            if capital(word[1]):
                for letter in word[2:]:
                    if not capital(letter):
                        return False
            else:
                for letter in word[2:]:
                    if capital(letter):
                        return False
            return True
