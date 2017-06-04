class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums) {
        // write your code here
        int rlt = nums[0]; 
        int n = 0;
        for(int i = 0; i < nums.size(); i++){  
            if(rlt == nums[i])  n++; else n--;
            if (n == 0) rlt = nums[i+1];
        }  
        return rlt; 
    }
};