# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        # inorder = (left, root, right)
        # preorder = (root, left, right)
        # postorder = (left, right, root)
        
        ans = []
        def recur(node):
            if node:
                recur(node.left)
                ans.append(node.val)
                recur(node.right)
        recur(root)
        return ans
