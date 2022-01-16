# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. 
# You need to merge the two trees into a new binary tree. 
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of the new tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        
        if not root1:
            return root2
        
        def recur(node1, node2, pre=None, flg=-1):
            if node1 and node2:
                node1.val = node1.val + node2.val
                recur(node1.left, node2.left, node1, 0)
                recur(node1.right, node2.right, node1, 1)
            elif node1:
                pass
            elif node2:
                if flg == 0:
                    pre.left = node2
                else:
                    pre.right = node2
            else:
                pass
        
        recur(root1, root2)
        return root1
