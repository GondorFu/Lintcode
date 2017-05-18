class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        if k == 0:
            return A
        i = 1
        A = ['0'] + list(A)
        while k > 0 and i < len(A):
            if A[i] < A[i-1]:
                A.pop(i-1)
                k -= 1
                i -= 1
            else:
                i += 1
        while k > 0 and len(A) > 0:
            A.pop()
            k -= 1
        while len(A) > 0 and A[0] == '0':
            A.pop(0)
        A = ''.join(A)
        return A