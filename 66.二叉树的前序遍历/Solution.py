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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        rlt = []
        if root == None:
            return rlt
        q = [root]
        while len(q) > 0:
            p = q.pop()
            rlt.append(p.val)
            if p.right != None:
                q.append(p.right)
            if p.left != None:
                q.append(p.left)
        return rlt