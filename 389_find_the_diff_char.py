# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        approach:
        sorting
        '''
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
        
        '''
        approach:
        brutal force
        
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        for c in t:
            m[c] -= 1
            if m[c] == 0:
                del m[c]
        return list(m.keys())[0]
        '''
