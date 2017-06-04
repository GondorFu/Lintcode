class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        rlt = self._permuteUnique(nums)
        return rlt
    
    def _permuteUnique(self, nums):
        rlt = []
        if len(nums) in [0, 1]:
            rlt.append(nums)
            return rlt
        for i, v in enumerate(nums):
            if i != 0 and v == nums[i-1]:
                continue
            snums = nums[:i] + nums[i+1:]
            srlt = self._permuteUnique(snums)
            for vv in srlt:
                vv.append(v)
                rlt.append(vv)
        return rlt
