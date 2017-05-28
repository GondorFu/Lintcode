'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        s = sorted(connections, key = lambda x: (x.cost, x.city1, x.city2))
        self.index = {}
        rlt = []
        count = 0
        for v in s:
            if v.city1 == v.city2:
                continue
            if v.city1 not in self.index and v.city2 not in self.index:
                self.index[v.city1] = v.city1
                self.index[v.city2] = v.city1
                count += 1
                rlt.append(v)
            elif v.city1 in self.index and v.city2 not in self.index:
                self.index[v.city2] = self.find_index(v.city1)
                rlt.append(v)
            elif v.city1 not in self.index and v.city2 in self.index:
                self.index[v.city1] = self.find_index(v.city2)
                rlt.append(v)
            else:
                vi = self.find_index(v.city1)
                vj = self.find_index(v.city2)
                if vi != vj:
                    count -= 1
                    self.index[vj] = vi
                    rlt.append(v)
        if count == 1 or count == 0:
            return rlt
        return []
        
        
                
    def find_index(self, vi):
        if self.index[vi] != vi:
            self.index[vi] = self.find_index(self.index[vi])
        return self.index[vi]