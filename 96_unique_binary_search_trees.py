# Given an integer n, return the number of structurally unique BST's (binary search trees) 
# which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        dp = dict()
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            loop = i // 2
            odd = i % 2 == 1
            count = 0
            for j in range(0, loop):
                count += 2 * (dp[j] * dp[i-1-j])
            if odd:
                count += dp[loop] * dp[loop]
            dp[i] = count
        
        return dp[n]
