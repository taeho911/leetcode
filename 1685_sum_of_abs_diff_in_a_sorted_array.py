# You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums such 
# that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        sums = [0] * (len(nums) + 1)
        sums[1] = nums[0]
        for i in range(1, len(nums)):
            sums[i+1] = nums[i] + sums[i]
            
        ans = [0] * len(nums)
        for i in range(len(nums)):
            l_len = i
            r_len = len(nums) - i - 1
            ans[i] = ((l_len * nums[i]) - sums[i]) \
                + ((sums[-1] - sums[i+1]) - (r_len * nums[i]))
        
        return ans
