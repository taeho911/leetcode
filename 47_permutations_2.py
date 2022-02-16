# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def backtrack(combination, counter):
            if len(combination) == len(nums):
                ans.append(list(combination))
            else:
                for num in counter:
                    if counter[num] > 0:
                        combination.append(num)
                        counter[num] -= 1
                        
                        backtrack(combination, counter)
                        
                        combination.pop()
                        counter[num] += 1
        
        backtrack([], Counter(nums))
        return ans
