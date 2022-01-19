# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        ans = [0]
        def dfs(node, i):
            if not node:
                ans[0] = max(ans[0], i)
                return
            dfs(node.left, i+1)
            dfs(node.right, i+1)
            
        dfs(root, 0)
        return ans[0]