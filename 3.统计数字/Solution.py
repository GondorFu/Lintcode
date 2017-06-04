class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        count = 0
        for i in range(n+1):
            if i == 0 and k == 0:
                count += 1
            while i != 0:
                n = i%10
                if n == k:
                    count += 1
                i = i//10
        return count