class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0. 
     */
    int binarySearch(vector<int> &array, int target) {
        // write your code here
        long long r = array.size() - 1;
        long long l = 0;
        long long mid;
        while(l < r){
            mid = (l + r)/2;
            if(array[mid] == target)
                r = mid;
            else if(array[mid] < target)
                l = mid + 1;
            else
                r = mid - 1;
        }
        if(array[r] == target) return r;
        return -1;
    }
};