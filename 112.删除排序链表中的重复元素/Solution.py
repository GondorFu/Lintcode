"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head == None:
            return None
        p1, p2 = head, head.next
        while p2 != None:
            if p1.val != p2.val:
                p1.next = p2
                p1 = p2
            p2 = p2.next
        p1.next = None
        return head