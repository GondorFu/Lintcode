class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        rlt = []
        if len(nums) in [0, 1]:
            rlt.append(nums)
            return rlt
        for i, v in enumerate(nums):
            snums = nums[:i] + nums[i+1:]
            srlt = self.permute(snums)
            for vv in srlt:
                vv.append(v)
                rlt.append(vv)
        return rlt
        
