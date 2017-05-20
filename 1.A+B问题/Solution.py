class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: The sum of a and b
    """

    def aplusb(self, a, b):
        # write your code here
        while b != 0:
            x = a ^ b 
            y = (a & b) << 1
            a = x
            b = y 
        return a
        
s = Solution()
s.aplusb(100, -100)