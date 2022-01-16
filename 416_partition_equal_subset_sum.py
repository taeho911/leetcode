# Given a non-empty array nums containing only positive integers, 
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Brutal force
class Solution:
    def canPartition(self, nums):
        self.ans = False
        
        def devide(i, left, right):
            if self.ans:
                return
            
            if i >= len(nums):
                if left == right:
                    self.ans = True
                return
            
            devide(i+1, left+nums[i], right)
            devide(i+1, left, right+nums[i])
        
        devide(1, nums[0], 0)
        return self.ans
