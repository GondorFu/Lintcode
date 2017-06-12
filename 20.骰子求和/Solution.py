class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        srlt = self._dicesSum(n)
        i = n
        rlt = []
        while i <= 6*n:
            rlt.append((i, srlt[i]))
            i += 1
        return rlt

    def _dicesSum(self, n):    
        c = 1.0/6
        if n == 1:
            return [c for i in range(6*n+1)]
        l = [0 for i in range(6*n+1)]
        sl = self._dicesSum(n-1)
        i = n - 1
        while i <= 6*n-6:
            l[i+1] += sl[i]*c
            l[i+2] += sl[i]*c
            l[i+3] += sl[i]*c
            l[i+4] += sl[i]*c
            l[i+5] += sl[i]*c
            l[i+6] += sl[i]*c
            i += 1
        return l
            