# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums):
        for n in set(nums):
            if nums.count(n) == 1:
                return n

class Solution_0:
    def singleNumber(self, nums):
        ans = 0
        for n in set(nums):
            # bitwise operator ^: XOR
            ans = ans ^ n
        return ans
