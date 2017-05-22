# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        p1 = l1
        p2 = l2
        l = ListNode(0)
        p = l
        c = 0
        while p1 != None and p2 != None:
            p.next = ListNode(p1.val + p2.val + c)
            c = 0
            if p.next.val >= 10:
                p.next.val %= 10
                c = 1
            p = p.next
            p1 = p1.next
            p2= p2.next
            
                
        while p1 != None:
            p.next = ListNode(p1.val + c)
            c = 0
            if p.next.val >= 10:
                p.next.val %= 10
                c = 1
            p1 = p1.next
            p = p.next
            
        while p2 != None:
            p.next = ListNode(p2.val + c)
            c = 0
            if p.next.val >= 10:
                p.next.val %= 10
                c = 1
            p2 = p2.next
            p = p.next
        
        if c == 1:
            p.next = ListNode(1)
        return l.next