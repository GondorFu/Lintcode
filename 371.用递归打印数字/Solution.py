class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        # write your code here
        l = [i for i in range(10)]
        if n == 0:
            return []
        if n == 1:
            return l[1:10]
        N_1 = self.numbersByRecursion(n-1)
        return l[1:10] + [i*10 +j for i in N_1 for j in l]