# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        def backtrack(comb: list[int], total: int):
            if total == target:
                ans.append(list(comb))
            elif total > target:
                return
            
            for n in candidates:
                if n > target:
                    break
                if comb and n < comb[-1]:
                    continue
                comb.append(n)
                backtrack(comb, total + n)
                comb.pop()
                
        backtrack([], 0)
        return ans
