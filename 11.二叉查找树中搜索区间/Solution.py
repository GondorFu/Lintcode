"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        rlt = []
        if root == None:
            return rlt
        if root.val >= k1:
            rlt += self.searchRange(root.left, k1, k2)
        if root.val >= k1 and root.val <= k2:
            rlt.append(root.val)
        if root.val <= k2:
            rlt += self.searchRange(root.right, k1, k2)
        return rlt