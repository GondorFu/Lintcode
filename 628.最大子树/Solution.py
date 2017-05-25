class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the maximum weight node
    def findSubtree(self, root):
        # Write your code here
        sum, rlt, maxSum = self.travel(root)
        return rlt
        
    def travel(self, root):
        if root == None:
            return 0, None, 0
        suml, rltl, maxSuml = self.travel(root.left)
        sumr, rltr, maxSumr = self.travel(root.right)
        if rltl == None and rltr == None:
            return root.val, root, root.val
        elif rltl == None:
            if root.val + sumr > maxSumr:
                return root.val + sumr, root, root.val + sumr
            return root.val + sumr, rltr, maxSumr
        elif rltr == None:
            if root.val + suml > maxSuml:
                return root.val + suml, root, root.val + suml
            return root.val + suml, rltl, maxSuml
        else:
            if root.val + suml + sumr > maxSuml and root.val + suml + sumr > maxSumr:
                return root.val + suml + sumr, root, root.val + suml + sumr
            elif maxSuml > maxSumr:
                return root.val + suml + sumr, rltl, maxSuml
            else:
                return root.val + suml + sumr, rltr, maxSumr
        