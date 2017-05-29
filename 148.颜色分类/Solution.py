class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        p0, p2 = 0, len(nums)-1
        i = p0
        while i <= p2:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i] = 1
                i += 1
                nums[p0] = 0
                p0 += 1
            elif nums[i] == 2:
                nums[i] = 1
                i += 1
                while nums[p2] == 2:
                    p2 -= 1
                if nums[p2] == 0:
                    nums[p0] = 0
                    p0 += 1
                nums[p2] = 2
                p2 -= 1
        return
                    
                