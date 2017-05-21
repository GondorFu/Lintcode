class Solution:
    """
    @param: : A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """

    def maxDiffSubArrays(self, nums):
        # write your code here
        n = len(nums)
        lmax, lmin, rmax, rmin = [0], [0], [0], [0]
        for v in nums:
            if lmax[-1] > 0:
                lmax.append(lmax[-1] + v)
            else:
                lmax.append(v)
            if lmin[-1] < 0:
                lmin.append(lmin[-1] + v)
            else:
                lmin.append(v)
                
        for v in nums[::-1]:
            if rmax[-1] > 0:
                rmax.append(rmax[-1] + v)
            else:
                rmax.append(v)
            if rmin[-1] < 0:
                rmin.append(rmin[-1] + v)
            else:
                rmin.append(v)
        
        rlt = 0       
        for i in range(1,n):
            if lmax[i] - rmin[n-i] > rlt:
                rlt = lmax[i] - rmin[n-i]
            if rmax[n-i] - lmin[i] > rlt:
                rlt = rmax[n-i] - lmin[i]
        return rlt
                
            
                
            