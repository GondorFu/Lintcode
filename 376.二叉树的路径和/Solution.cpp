"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        rlt = []
        if root == None:
            return rlt
        rlt += self.binaryTreePathSum(root.left, target-root.val)
        rlt += self.binaryTreePathSum(root.right, target-root.val)
        if len(rlt) != 0:
            for i, v in enumerate(rlt):
                if isinstance(v, list):
                    rlt[i] = [root.val] + v
                else:
                    rlt[i] = [root.val] + [v]
        if root.val == target and root.right == None and root.left == None:
            rlt += [[root.val]]
        return rlt