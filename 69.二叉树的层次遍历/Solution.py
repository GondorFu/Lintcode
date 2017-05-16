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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        res = list()
        if root == None:
            return res
        q = list()
        q.append(root)
        while len(q) > 0:
            n = len(q)
            t = list()
            for v in q[0:n]:
                t.append(v.val)
                if v.left != None:
                    q.append(v.left)
                if v.right != None:
                    q.append(v.right)        
            res.append(t)
            q[0:n] = []


        
        return res
            
            