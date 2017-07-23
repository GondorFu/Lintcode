class Solution:
    # @param {int} n an integer
    # @return {int} an integer
    def dropEggs(self, n):
        # Write your code here
        return int(math.floor((math.sqrt(8*n-7)+1)/2))