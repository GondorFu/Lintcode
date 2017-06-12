class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        # Write your code here
        if root == None:
            return root
        rlt = root
        rlt = self._maxNode(rlt, root)
        return rlt
    
    def _maxNode(self, rlt, root):
        if root == None:
            return rlt
        rlt = self._maxNode(rlt, root.right)
        rlt = self._maxNode(rlt, root.left)
        if root.val > rlt.val:
            return root
        return rlt