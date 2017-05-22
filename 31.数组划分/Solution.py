class Solution:
    """
    @param: : The integer array you should partition
    @param: : An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        n = len(nums)
        i, j = 0, n-1
        while i < j:
            while i < j and nums[i] < k:
                i += 1
            while i < j and nums[j] >= k:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        if i == n-1:
            return i+1
        return i