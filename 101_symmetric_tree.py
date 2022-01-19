# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        
        stack = [[root.left, root.right]]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if (l and not r) or (not l and r) or (l.val != r.val):
                return False
            
            stack.append([l.left, r.right])
            stack.append([l.right, r.left])
        
        return True