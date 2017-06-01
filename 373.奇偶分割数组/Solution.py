class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        i, j = 0, len(nums)-1
        
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        return
