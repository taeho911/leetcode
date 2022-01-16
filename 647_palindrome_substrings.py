# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        ans = 0
        
        def get_longest_palindrome(s, start, end):
            n = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                n += 1
            return n
        
        for i in range(len(s)):
            ans += get_longest_palindrome(s, i, i) + get_longest_palindrome(s, i, i+1)
        
        return ans
