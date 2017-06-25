class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCostII(self, costs):
        # Write your code here
        if len(costs) == 0:
            return 0
        n = len(costs[0])
        rlt = [0 for i in range(n)]
        for v in costs:
            vMin = min(rlt)
            count = rlt.count(vMin)
            if count == 1:
                index = rlt.index(vMin)
                vMin2 = min(rlt[0:index] + rlt[index+1:])
                rlt = [vMin for i in range(n)]
                rlt[index] = vMin2
            else:
                rlt = [vMin for i in range(n)]
            rlt = [a+b for a,b in zip(v, rlt)]
        return min(rlt)