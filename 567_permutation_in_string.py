# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

from collections import deque

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_counter = {}
        for char in s1:
            s1_counter[char] = s1_counter.get(char, 0) + 1
        
        q = deque()
        for i in range(len(s2)):
            if s2[i] in s1_counter:
                if s1_counter[s2[i]] > 0:
                    s1_counter[s2[i]] -= 1
                    q.append(s2[i])
                else:
                    while q and q[0] != s2[i]:
                        s1_counter[q.popleft()] += 1
                    if q:
                        q.append(q.popleft())
            else:
                while q:
                    s1_counter[q.popleft()] += 1
            if len(q) == s1_len:
                return True
        
        return False
