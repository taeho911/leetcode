# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        s_len = len(s)
        p_len = len(p)
        
        def is_anagram(a, b):
            x = "".join(sorted(a))
            y = "".join(sorted(b))
            if x != y:
                return False
            return True
        
        matched = False
        for i in range(0, s_len - p_len + 1):
            if not s[i] in p:
                matched = False
                continue
            if matched and s[i + p_len - 1] == s[i-1]:
                ans.append(i)
                continue
            if is_anagram(s[i:i+p_len], p):
                ans.append(i)
                matched = True
            else:
                matched = False
        
        return ans
