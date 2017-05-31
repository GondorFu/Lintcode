class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        if num < 0:
            count += 1
            num &= 2**31 - 1
        
        while num != 0:
            num = num & (num - 1)
            count += 1
        return count
