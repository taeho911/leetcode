# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        memo = [[]]
        for n in nums:
            for ls in memo.copy():
                memo.append(ls + [n])
        return memo
