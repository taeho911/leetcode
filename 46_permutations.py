# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def recur(l, r):
            if l == r:
                ans.append(nums.copy())
            else:
                for i in range(l, len(nums)):
                    nums[i], nums[l] = nums[l], nums[i]
                    recur(l+1, r)
                    nums[i], nums[l] = nums[l], nums[i]
        
        recur(0, len(nums) - 1)
        return ans
