class Solution:
    # @param {int} num a positive number
    # @return {boolean} true if it's a palindrome or false
    def palindromeNumber(self, num):
        # Write your code here
        s1 = str(num)
        s2 = s1[::-1]
        if s1 == s2:
            return True
        else:
            return False