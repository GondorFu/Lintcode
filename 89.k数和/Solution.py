class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        dp = [[0 for i in range(target+1)] for i in range(k+1)]
        dp[0][0] = 1
        for v in A:
            for j in range(target, v-1, -1):
                for i in range(1, k+1):
                    dp[i][j] = dp[i][j] + dp[i-1][j-v]
                     
        return dp[k][target]