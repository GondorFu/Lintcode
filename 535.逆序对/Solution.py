class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, A):
        # Write your code here
        A, rlt = self.merge_sort(A)
        return rlt
        
    def merge_sort(self, A):
        n = len(A)
        count = 0
        if n in [0, 1]:
            return A, count
        left, countl = self.merge_sort(A[0:n//2])
        count += countl
        right, countr= self.merge_sort(A[n//2:])
        count += countr
        A = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A.append(left[i])
                i += 1
            else:
                A.append(right[j])
                j += 1
                count += len(left) - i
        A = A + left[i:] + right[j:]
        return A, count