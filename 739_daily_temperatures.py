# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        t_len = len(temperatures)
        if t_len == 1:
            return [0]
        
        ans = [0] * t_len
        search = []
        
        for i in range(1, t_len):
            if temperatures[i-1] < temperatures[i]:
                ans[i-1] = 1
                while search:
                    t = search.pop()
                    if temperatures[t] < temperatures[i]:
                        ans[t] = i - t
                    else:
                        search.append(t)
                        break
            else:
                search.append(i-1)
        
        return ans