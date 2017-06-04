class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if s != None and len(s) != 0:
            left = 0
            right = len(s) - 1
            offset = offset%(right+1)
            self.rotateStr(s,0,right - offset)
            self.rotateStr(s,right - offset + 1,right)
            self.rotateStr(s,0,right)
        
        
    def rotateStr(self,s,left,right):
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
	    