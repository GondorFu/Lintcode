class Solution {
public:
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        // write your code here
        int m = matrix.size();
        if(m == 0)
            return false;        
            
        int n = matrix[0].size();

        int l = 0, r = m*n-1;
        int mid = (r + l)/2;
        int row = 0, col = 0;
        while(l < r){
            row = mid/n;
            col = mid%n;
            if(matrix[row][col] == target)
                break;
            else if(matrix[row][col] > target)
                r = mid - 1;
            else
                l = mid + 1;
                
            mid = (l + r)/2;
        }
        
        row = mid/n;
        col = mid%n;
        if(matrix[row][col] != target || row < 0 || col < 0)
            return false;
        else
            return true;
        
    }
};
