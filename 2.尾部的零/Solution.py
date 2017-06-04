class Solution:
    # @param n a integer
    # @return as a integer
    def trailingZeros(self, n):
        count = 0
        while n > 1:
            n /= 5
            count += n
        return count
        