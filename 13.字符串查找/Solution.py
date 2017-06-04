class Solution:
    """
    @param: : source string to be scanned.
    @param: : target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1
        ns, nt = len(source), len(target)
        if nt == 0:
            return 0
        if ns == 0:
            return -1
        next = self.getNext(target)
        i, j = 0, 0
        while i < ns and j < nt:
            if j == -1 or source[i] == target[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == nt:
            return i - nt
        return -1
        
    def getNext(self, target):
        nt = len(target)
        next = [-1 for i in range(nt + 1)]
        i, j = 0, -1
        while i < nt:
            if j == -1 or target[i] == target[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return next