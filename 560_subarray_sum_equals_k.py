# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

from collections import defaultdict

class Solution:
    # basic idea is that if sum[i] - sum[j] = k, then the sum of numbers between index i and j is k.
    # eg:
    # sum[i] = 10 --> num[i+1] = 6 --> num[i+2] = 8 --> nums[j] = -12, sum[j] = 12
    # cumulative sum goes from 10 to 12 so sum of elements between i and j is 2 (6 + 8 -12).
	
	# using this logic, we maintain dictionary with cumulative sum as key and value as number of time same sum occurs.
	# we also check if key sum-k is present, to check and add count of number of times subarray with sum k has occurred up to 
	# the current index.
    
    def subarraySum(self, nums: list[int], k: int) -> int:
        count, sum = 0, 0
        dic = defaultdict(int) # key: sum, value: count of times same sum occurs
        dic[0] = 1
        for i in range(0, len(nums)):
            sum += nums[i]
            if (sum-k) in dic:
                count += dic.get(sum - k)
            dic[sum] = dic.get(sum, 0) + 1
        return count
