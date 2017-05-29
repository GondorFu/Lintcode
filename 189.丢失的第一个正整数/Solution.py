class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        n = len(A)
        i = 0
        while i < n:
            if A[i] >= 1 and A[i] <= n and A[i] != i+1 and A[A[i]-1] != A[i]:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
            else:
                i += 1
        n = 1        
        for v in A:
            if v != n:
                break
            n += 1
        return n
