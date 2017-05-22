"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if head == None:
            return None
        p = head
        pp = p.next
        while pp != None:
            ppp = pp.next
            pp.next = p
            p = pp
            pp = ppp
            
        head.next = None
        return p
        
            