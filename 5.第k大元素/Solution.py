class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        n = len(A)
        i, j = 0, n-1
        v = A[i]
        while i < j:
            while i < j and A[j] <= v:
                j -= 1
            A[i] = A[j]
            while i < j and A[i] >= v:
                i += 1
            A[j] = A[i]
        A[i] = v
        if i+1 == k:
            return A[i]
        elif i+1 > k:
            return self.kthLargestElement(k, A[0:i])
        else:
            return self.kthLargestElement(k-1-i, A[i+1:])
            
        