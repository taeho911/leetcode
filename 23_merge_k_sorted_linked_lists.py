# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge2Lists(self, l1, l2):
        head = ListNode()
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                while l1 and l1.val <= l2.val:
                    p = l1
                    l1 = l1.next
            else:
                p.next = l2
                while l2 and l2.val <= l1.val:
                    p = l2
                    l2 = l2.next
                
        if not l1 and not l2:
            pass
        elif l1:
            p.next = l1
        elif l2:
            p.next = l2
        
        return head.next
        
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        ls = []
        for i in range(1, len(lists), 2):
            merged = self.merge2Lists(lists[i-1], lists[i])
            ls.append(merged)
        if len(lists) % 2 == 1:
            ls.append(lists[-1])
        result = self.mergeKLists(ls)
        return result

class Solution_0(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next