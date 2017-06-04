class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
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
        for v in srlt:
            rlt.append(v + [S[-1]])
        return rlt