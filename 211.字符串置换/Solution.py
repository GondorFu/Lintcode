class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        if len(A) != len(B):
            return False
        d = {}
        for v in A:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1
                
        for v in B:
            if v in d and d[v] > 0:
                d[v] -= 1
            else:
                return False
        return True