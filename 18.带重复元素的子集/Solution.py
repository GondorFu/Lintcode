class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        S.sort()
        rlt = self._subsets(S)
        return rlt
        
    def _subsets(self, S):
        rlt = []
        if len(S) == 0:
            return [[]]
        if len(S) == 1:
            rlt.append([])
            rlt.append(S)
            return rlt
        srlt = self._subsets(S[:-1])
        if S[-2] != S[-1]:
            rlt += srlt
        else:
            for v in srlt:
                if len(v) == 0 or v[-1] != S[-1]:
                    rlt.append(v)
                else:
                    break
        for v in srlt:
            rlt.append(v + [S[-1]])
        return rlt