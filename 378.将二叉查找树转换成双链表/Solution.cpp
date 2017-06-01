"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        head = DoublyListNode(0)
        if root ==  None:
            return head.next
        nodeLeft = self.bstToDoublyList(root.left)
        if nodeLeft != None:
            head.next, nodeLeft.prev = nodeLeft, head
        
        p = head
        while p.next != None:
            p = p.next
        nodeRoot = DoublyListNode(root.val)
        p.next, nodeRoot.prev = nodeRoot, p
        
        nodeRight = self.bstToDoublyList(root.right)
        if nodeRight != None:
            while p.next != None:
                p = p.next
            p.next, nodeRight.prev = nodeRight, p
        head.next.prev = None
        return head.next
        
        
        
        