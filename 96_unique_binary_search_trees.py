# Given an integer n, return the number of structurally unique BST's (binary search trees) 
# which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            loop = i // 2
            odd = i % 2 == 1
            for j in range(0, loop):
                dp[i] += 2 * (dp[j] * dp[i-1-j])
            if odd:
                dp[i] += dp[loop] * dp[loop]
        
        return dp[n]
