# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first 
# if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        m = {}
        prc = [0] * numCourses
        for p in prerequisites:
            if p[1] in m:
                m[p[1]].append(p[0])
            else:
                m[p[1]] = [p[0]]
            prc[p[0]] += 1
        
        q = deque()
        count = 0
        for i in range(numCourses):
            if prc[i] == 0:
                q.append(i)
                count += 1
        
        while q:
            c = q.popleft()
            if c in m:
                for next_c in m[c]:
                    prc[next_c] -= 1
                    if prc[next_c] == 0:
                        q.append(next_c)
                        count += 1
        
        return count == numCourses
