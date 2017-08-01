class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        n = len(nums)
        nums.sort()
        i = 1
        while i < n-1:
            nums.insert(i, nums.pop())
            i += 2
        return