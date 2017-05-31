"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        left = self.buildTree(preorder[1:index+1], inorder[0:index])
        right = self.buildTree(preorder[index+1:], inorder[index+1:])
        root.left = left
        root.right = right
        return root