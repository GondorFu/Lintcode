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
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        rlt = list()
        if root == None:
            return rlt
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
            if len(rlt) % 2 == 1:
                t.reverse()
            rlt.append(t)
            q[0:n] = []
        return rlt