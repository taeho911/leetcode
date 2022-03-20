# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. 
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
# If it cannot be done, return -1.

from collections import defaultdict, Counter
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        c = defaultdict(int)
        for i in range(len(tops)):
            if tops[i] == bottoms[i]:
                c[tops[i]] += 1
            else:
                c[tops[i]] += 1
                c[bottoms[i]] += 1
        
        candi = []
        for k, v in c.items():
            if v == len(tops):
                candi.append(k)
        
        if not candi:
            return -1
        else:
            ct = Counter(tops)
            cb = Counter(bottoms)
            max_occur = 0
            for item in candi:
                max_occur = max(max_occur, ct.get(item, 0), cb.get(item, 0))
            return len(tops) - max_occur
        