class Solution {
public:
    /**    
     * @param A: a vector of integers
     * @return: an integer
     */
    int firstMissingPositive(vector<int> A) {
        // write your code here
        int n = A.size();
        
        for(int i=0; i<n; ){
            if(A[i] == i+1)
                i++;
            else if(A[i]>=1 && A[i]<=n && A[A[i]-1] != A[i])
                swap(A[A[i]-1], A[i]);
            else
                i++;
        }
        
        for(int i=0; i<n; i++)
            if(A[i] != i+1)
                return i+1;
                
        return n+1;
    }
};