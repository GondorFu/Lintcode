class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):
        # Write your code here
        n = len(nums)
        if n == 0: return 0
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        
        for j in range(1, n+1):
            for i in range(j, 0, -1):
                for k in range(i, j+1):
                    sum = dp[i][k-1]+ nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j]
                    if sum > dp[i][j]:
                        dp[i][j] = sum
        
        return dp[1][n]
        