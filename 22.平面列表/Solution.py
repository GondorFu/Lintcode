class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if not isinstance(nestedList, list):
            return [nestedList]
        rlt = []
        while len(nestedList) > 0:
            v = nestedList.pop(0)
            if isinstance(v, list):
                for vv in v[::-1]:
                    nestedList.insert(0, vv)
            else:
                rlt.append(v)
        return rlt