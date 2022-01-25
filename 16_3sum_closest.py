# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

import sys

class Solution:
    def threeSumClosest(self, nums, target):
        ans = None
        min_diff = sys.maxsize
        dp = dict()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                two_sum = nums[i] + nums[j]
                if two_sum in dp:
                    continue
                    
                for k in range(j+1, len(nums)):
                    three_sum = two_sum + nums[k]
                    abs_diff = abs(three_sum - target)
                    if abs_diff == 0:
                        return three_sum
                    elif abs_diff < min_diff:
                        min_diff = abs_diff
                        ans = three_sum
                    dp[two_sum] = three_sum
        
        return ans

class Solution_0:
    def threeSumClosest(self, nums, target):
        nums.sort()
        output=sys.maxsize
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: continue
            l=i+1
            r=len(nums)-1
            while (l<r):
                s=nums[i]+nums[l]+nums[r]
                if s==target: return s
                if abs(s-target)<abs(output-target):
                    output=s
                if s<target:
                    l+=1
                else:
                    r-=1
        return output
