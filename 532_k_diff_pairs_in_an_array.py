# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#   - 0 <= i < j < nums.length
#   - |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

class Solution:
    def findPairs(self, nums, k: int) -> int:
        ds = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k and (nums[j], nums[i]) not in ds:
                    ds.add((nums[i], nums[j]))
        return len(ds)

class Solution_0:
    def findPairs(self, nums, k: int) -> int:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        ans = 0
        for key in counter.keys():
            if (k > 0 and key + k in counter) or (k == 0 and counter.get(key + k, 0) > 1):
                ans += 1
        return ans