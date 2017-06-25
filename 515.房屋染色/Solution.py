class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        rlt = [0, 0, 0]
        rlt_temp = [0, 0, 0]
        for v in costs:
            rlt_temp[0] = v[0] + min(rlt[1], rlt[2])
            rlt_temp[1] = v[1] + min(rlt[0], rlt[2])
            rlt_temp[2] = v[2] + min(rlt[0], rlt[1])
            rlt = [rlt_temp[0], rlt_temp[1], rlt_temp[2]]
        return min(rlt)