# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        inorder = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        dfs(root)
        
        return inorder[k-1]

class Solution_0:
    def kthSmallest(self, root, k):
        stack = []
        pointer = root
        
        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            pointer = node.right