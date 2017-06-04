"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        c = n - m
        p = ListNode(0, head)
        headp = p
        while m-1 > 0:
            p = p.next
            m -= 1
        pm = p.next
        pmm = None
        if c > 0:
            pmm = pm.next
        while c > 0:
            c -= 1
            pmmm = pmm.next
            pmm.next = pm
            pm, pmm = pmm, pmmm
            
        p.next.next = pmm
        p.next = pm
        return headp.next
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
