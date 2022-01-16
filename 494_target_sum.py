# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums 
# and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

class Solution:
    def subsetsum(self, nums, sum):
        dp = [[0 for j in range(sum+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(sum+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][sum]
    
    def findTargetSumWays(self, nums, target):
        diffsum = sum(nums) - target
        if diffsum < 0:
            return 0
        if diffsum%2 != 0:
            return 0
        return self.subsetsum(nums, diffsum//2)

class Solution_0:
    def findTargetSumWays(self, nums, target):
        cache = {}
        
        def backtrack(i, total):
            if i >= len(nums):
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            return cache[(i, total)]
        
        return backtrack(0, 0)

if __name__ == '__main__':
    testcases = [
        {'nums': [1,1,1,1,1], 'target': 3},
        {'nums': [1,2,2,4,4,6,7,8,9], 'target': 27}
    ]
    sol = Solution_0()
    for testcase in testcases:
        print(sol.findTargetSumWays(testcase['nums'], testcase['target']))
