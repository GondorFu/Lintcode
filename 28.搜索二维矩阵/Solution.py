class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        i, j = 0, m-1
        while i < j:
            mid = (i + j)/2
            if mid == i:
                mid = j
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                i = mid
            elif matrix[mid][0] > target:
                j = mid - 1
        k = i
        i, j = 0, n-1
        while i < j:
            mid = (i + j)/2
            if matrix[k][mid] == target:
                return True
            elif matrix[k][mid] < target:
                i = mid + 1
            elif matrix[k][mid] > target:
                j = mid - 1
        if matrix[k][i] == target:
            return True
        return False
