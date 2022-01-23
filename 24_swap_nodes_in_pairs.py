# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        ans = ListNode()
        prev_prev_node = ans
        prev_node = head
        curr_node = head.next
        
        while curr_node:
            prev_prev_node.next = curr_node
            prev_node.next = curr_node.next
            curr_node.next = prev_node
            
            prev_prev_node = prev_node
            prev_node = prev_node.next
            curr_node = prev_node.next if prev_node else None
        
        return ans.next

class Solution_0:
    def swapPairs(self, head):
        # first: non recursive way
        # if element is None or only one
        if not (head and head.next):
            return head
        # Nodes to be swapped
        cur = head
        nex = head.next
        
        cur.next = self.swapPairs(nex.next)
        nex.next = cur
        
        return nex
