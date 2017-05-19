class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        mLen = 0
        rlt = list()
        for v in dictionary:
            if len(v) > mLen:
                rlt = []
                mLen = len(v)
                rlt.append(v)
            elif len(v) == mLen:
                rlt.append(v)
                
        return rlt