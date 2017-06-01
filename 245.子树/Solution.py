"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if T2 == None:
            return True
        self.T2 = T2
        return self._isSubtree(T1, T2)

    def _isSubtree(self, T1, T2):    
        if T1 == None and T2 == None:
            return True
        if T2 == None or T1 == None:
            return False
        if T1.val == T2.val and self._isSubtree(T1.left, T2.left) and self._isSubtree(T1.right, T2.right):
            return True
        if self._isSubtree(T1.left, self.T2) or self._isSubtree(T1.right, self.T2):
            return True
        return False
            
                
        