class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        rlt = nums[0]
        count = 0
        for i, v in enumerate(nums):
            if v == rlt:
                count += 1
            else:
                count -= 1
                if count == 0:
                    rlt = nums[i+1]
        return rlt
