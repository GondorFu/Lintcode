class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        rlt = [0, 0, 1]
        i = 2
        while i < n:
            rlt.append(rlt[i] + rlt[i-1])
            i += 1
        return rlt[n]
