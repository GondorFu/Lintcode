class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        i, j = 0, 0
        rlt = []
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                rlt.append(A[i])
                i += 1
            else:
                rlt.append(B[j])
                j += 1
        rlt += A[i:] + B[j:]
        return rlt