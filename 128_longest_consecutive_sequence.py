# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(nums)
        ans = 1
        temp = 1
        
        for i in range(1, len(sorted_nums)):
            diff = sorted_nums[i] - sorted_nums[i-1]
            
            if diff == 1:
                temp += 1
            elif diff == 0:
                continue
            elif diff > 1:
                ans = max(ans, temp)
                temp = 1
        
        ans = max(ans, temp)
                
        return ans
