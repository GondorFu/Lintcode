class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        if len(nums) < k or len(nums) == 0:
            return []
        rlt = [sum(nums[0:k])]
        i = k
        while i < len(nums):
            rlt.append(rlt[-1] - nums[i-k] + nums[i])
            i += 1
        return rlt