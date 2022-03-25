# A company is planning to interview 2n people. 
# Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, 
# and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = sorted([(abs(ls[0] - ls[1]), i) for i, ls in enumerate(costs)], reverse=True)
        n = len(costs) // 2
        answer = 0
        a = 0
        b = 0
        sames = []
        
        for _, i in diff:
            if costs[i][0] == costs[i][1]:
                sames.append(i)
                continue
            
            if a == n:
                answer += costs[i][1]
                b += 1
                continue
            elif b == n:
                answer += costs[i][0]
                a += 1
                continue
                
            if costs[i][0] > costs[i][1]:
                answer += costs[i][1]
                b += 1
            elif costs[i][0] < costs[i][1]:
                answer += costs[i][0]
                a += 1
        
        for i in sames:
            if a == n:
                answer += costs[i][1]
            else:
                answer += costs[i][0]
        
        return answer

class Solution_0:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        total_cost = 0
        for i in range(len(costs)//2):
            total_cost += costs[i][1] + costs[i+len(costs)//2][0]
        return total_cost
