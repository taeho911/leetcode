# Given the root of a binary tree and an integer targetSum, 
# return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards 
# (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        dp = {}
        stack = []
        
        def backtrack(node):
            if node == None:
                return
            
            stack.append(node.val)
            
            # Calculate all possible sums
            for i in range(len(stack)):
                s_sum = sum(stack[i:])
                if s_sum in dp:
                    dp[s_sum] += 1
                else:
                    dp[s_sum] = 1
            
            backtrack(node.left)
            backtrack(node.right)
            
            stack.pop()
        
        backtrack(root)
        return dp.get(targetSum, 0)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_0:
    def pathSum(self, root, targetSum):
        if not root: return 0
        
        self.numOfPaths = 0
        visited = {0:1} # currSum: freq
        
        def dfs(node, prevSum):
            currSum = prevSum + node.val
            
            subSum = currSum - targetSum
            
            if subSum in visited:
                self.numOfPaths += visited[subSum]
            if currSum in visited:
                visited[currSum] += 1
            else:
                visited[currSum] = 1
                
            if node.left:
                dfs(node.left, currSum)
            if node.right:
                dfs(node.right, currSum)
                
            visited[currSum] -= 1
        
        dfs(root, 0)
        return self.numOfPaths