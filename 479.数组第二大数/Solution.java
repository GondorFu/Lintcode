public class Solution {
    /**
     * @param nums: An integer array.
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        /* your code */
        int m1, m2;
        if(nums[0] > nums[1]){
           m1 = nums[0];
           m2 = nums[1];
        } 
        else{
           m1 = nums[1];
           m2 = nums[0];
        }
        for(int i=2; i<nums.length; i++){
            if(nums[i] > m1) {m2 = m1; m1 = nums[i];}
            else if (nums[i] > m2) m2 = nums[i];
        }
        return m2;
    }
}