class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        d = {}
        for v in strs:
            v = ''.join(sorted(list(v)))
            if d.get(v, -1) == -1:
                d[v] = 1
            else:
                d[v] += 1
        rlt = [] 
        for v in strs:
            vm = ''.join(sorted(list(v)))
            if d[vm] > 1:
                rlt.append(v)
        return rlt