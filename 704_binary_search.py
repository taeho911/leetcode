# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            i = (r + l) // 2
            
            if nums[i] < target:
                l = i + 1
            elif nums[i] > target:
                r = i - 1
            else:
                return i
            
        return -1
