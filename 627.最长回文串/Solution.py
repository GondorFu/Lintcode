class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        # Write your code here
        d = dict()
        for v in s:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1
        b = 0
        rlt = 0
        for v in d.values():
            if v%2 == 0:
                rlt += v
            elif b == 0:
                b = 1
                rlt += v
            else:
                rlt += v - 1
        return rlt