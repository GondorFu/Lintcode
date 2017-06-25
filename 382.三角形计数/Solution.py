class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        rlt = 0
        S.sort()
        n = len(S)
        for i in range(0, n-2):
            for j in range(n-1, i+1, -1):
                target = S[j] - S[i]
                l, r = i+1, j-1
                while l < r:
                    m = (l + r)/2
                    if S[m] > target:
                        r = m
                    else:
                        l = m + 1
                if S[l] > target:
                    rlt += j - l
                        
        return rlt
        
                