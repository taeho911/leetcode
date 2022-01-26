# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1, root2):
        
        def dfs(node, ls):
            if not node:
                return
            dfs(node.left, ls)
            ls.append(node.val)
            dfs(node.right, ls)
        
        ls1 = []
        ls2 = []
        dfs(root1, ls1)
        dfs(root2, ls2)
        return sorted(ls1 + ls2)
