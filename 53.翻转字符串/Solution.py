class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        l = s.split(' ')
        rlt = list()
        for v in l[::-1]:
            if len(v) != 0:
                rlt.append(v)
        rlt = ' '.join(rlt)
        return rlt