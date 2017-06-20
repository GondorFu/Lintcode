"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        rlt = []
        if root == None:
            return rlt
        q = [root]
        while len(q) != 0:
            n = len(q)
            t = []
            for v in q[0:n]:
                t.append(v.val)
                if v.left != None:
                    q.append(v.left)
                if v.right != None:
                    q.append(v.right)        
            rlt.append(t)
            q[0:n] = []
        
        rlt.reverse()
        return rlt
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        