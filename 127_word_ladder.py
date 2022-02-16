# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
# beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, 
# return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        
        m = defaultdict(list)
        
        for w in wordList:
            for i in range(len(w)):
                prefix = w[:i]
                suffix = w[i+1:]
                m[prefix + '.' + suffix].append(w)
        
        q = deque([(1, beginWord)])
        visited = set()
        while q:
            l, w = q.popleft()
            for i in range(len(w)):
                prefix = w[:i]
                suffix = w[i+1:]
                for s in m[prefix + '.' + suffix]:
                    if s == endWord:
                        return l+1
                    elif s not in visited:
                        q.append((l+1, s))
                        visited.add(s)
        return 0
