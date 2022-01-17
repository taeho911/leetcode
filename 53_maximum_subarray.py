# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

import sys

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        mintotal = 0
        ans = -sys.maxsize
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            ans = max(ans, total - mintotal)
            mintotal = min(mintotal, total)
        return ans
