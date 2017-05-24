class Solution {
public:
    /**
     * @param A an array
     * @return total of reverse pairs
     */
    long long reversePairs(vector<int>& A) {
        // Write your code here
        long long count = 0;
        merge_sort(A, count);
        return count;
    }
    
    void merge_sort(vector<int>& A, long long& count){
        if(A.size() <= 1) return;
        
        int n = A.size()/2;
        vector<int> left(A.begin(), A.begin()+n);
        vector<int> right(A.begin()+n, A.end());
        merge_sort(left, count);
        merge_sort(right, count);
        
        A.clear();
        while(left.size() > 0 && right.size() > 0){
           if(left[0] > right[0]) {
               count = count + left.size();
               A.push_back(right[0]);
               right.erase(right.begin());
           }
           else{
               A.push_back(left[0]);
               left.erase(left.begin());
           }
        }
        while(left.size() > 0){
            A.push_back(left[0]);
            left.erase(left.begin());
        }
        while(right.size() > 0){
            A.push_back(right[0]);
            right.erase(right.begin());
        }
        return;   
    }
};


















