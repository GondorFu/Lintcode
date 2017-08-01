class Solution:
    # @param {int} m the number of eggs
    # @param {int} n the umber of floors
    # @return {int} the number of drops in the worst case
    def dropEggs2(self, m, n):
        # Write your code here
        dp = [[0 for i in range(m+1)], [1 for i in range(m+1)]]
        for i in range(2, n+1):
            dp.append([i for x in range(m+1)])
        
        for i in range(2, n+1):
            for j in range(2, m+1):
                for k in range(1, n+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[k-1][j-1], dp[i-k][j]))
                    
        return dp[n][m]
        
        