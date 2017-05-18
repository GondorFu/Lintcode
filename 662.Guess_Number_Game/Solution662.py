# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# you can call Guess.guess(num)

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        l, r = 1, n
        m = (l + r)//2
        while l <= r:
            res = Guess.guess(m)
            if res == 1:
                l = m + 1
            elif res == -1:
                r = m - 1
            else:
                break
            m = (l + r)//2
        return m