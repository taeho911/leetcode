# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

class Solution:
    def diameterOfBinaryTree(self, root):
        
        def get_depth(node, depth=0):
            if node == None:
                return depth-1
            return max(get_depth(node.left, depth+1), get_depth(node.right, depth+1))
        
        def get_diameter(node, max_dm=0):
            if node == None or (node.left == None and node.right == None):
                return 0
            elif node.left == None:
                return get_depth(node.right) + 1
            elif node.right == None:
                return get_depth(node.left) + 1
            
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            self_max_dm = left_depth + right_depth + 2
            
            return max(max_dm, self_max_dm, get_diameter(node.left, self_max_dm), get_diameter(node.right, self_max_dm))
        
        return get_diameter(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_0:
    def diameterOfBinaryTree(self, root):
        """
        Recursively explore the left and right nodes
        Update answer with the sum of l+r if larger than max
        return max(l,r) + 1, increment by 1 to account for the edge with parent node
        """
        self.ans = 0
        
        def depth(p):
            if not p:
                return 0
            l = depth(p.left)
            r = depth(p.right)
            
            self.ans = max(self.ans, l+r)
            return max(l,r) + 1
            
        depth(root)
        return self.ans