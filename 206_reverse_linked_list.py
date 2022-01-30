# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        stack = []
        ans = [head]
        def reverse(node):
            if not node:
                if stack:
                    ans[0] = stack.pop()
                return
            stack.append(node)
            reverse(node.next)
            if not stack:
                node.next = None
                return
            node.next = stack.pop()
        
        reverse(head)
        return ans[0]

class Solution_0:
    def reverseList(self, head):
        
        prev, curr = None, head
        
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
