# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        def recur(ls1, ls2, pre):
            if not ls1 and not ls2:
                return
            if not ls1:
                pre.next = ls2
                return
            if not ls2:
                pre.next = ls1
                return
                
            if ls1.val < ls2.val:
                pre.next = ListNode(val=ls1.val)
                recur(ls1.next, ls2, pre.next)
            elif ls1.val > ls2.val:
                pre.next = ListNode(val=ls2.val)
                recur(ls1, ls2.next, pre.next)
            else:
                pre.next = ListNode(val=ls1.val, next=ListNode(val=ls2.val))
                recur(ls1.next, ls2.next, pre.next.next)
        
        head = ListNode()
        if list1.val < list2.val:
            head.val = list1.val
            recur(list1.next, list2, head)
        elif list1.val > list2.val:
            head.val = list2.val
            recur(list1, list2.next, head)
        else:
            head.val = list1.val
            head.next = ListNode(val=list2.val)
            recur(list1.next, list2.next, head.next)
        
        return head
