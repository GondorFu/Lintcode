class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        n = len(nums)
        nn = []
        i = 0
        while (n+i) % 4 != 3:
            i += 1
            nn.append(n+i)
        rlt = reduce(lambda x, y: x^y, nums + nn)
        return rlt