"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        # Write your code here
        c = None
        if root == None:
            return c
        c = TreeNode(root.val)
        c.left = self.cloneTree(root.left)
        c.right = self.cloneTree(root.right)
        return c