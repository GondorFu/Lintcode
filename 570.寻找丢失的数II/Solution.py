class Solution:
    # @param {int} n an integer
    # @param {string} str a string with number from 1-n
    #                     in random order and miss one number
    # @return {int} an integer
    def findMissing2(self, n, str):
        # Write your code here
        m = len(str)
        stk = []
        sel = [True] + [False for i in range(n)]
        flag = False
        i = 0
        while i < m:
            if flag or i == m-1 or int(str[i:i+2]) < 10 or int(str[i:i+2]) > n:
                val = int(str[i])
                if sel[val]:
                    flag = True
                    j = stk.pop()
                    for k in range(j+2,i):
                        sel[int(str[k])] = False
                    sel[int(str[j:j+2])] = False
                    i = j
                else:
                    flag = False
                    sel[val] = True
                    i += 1
            else:
                val = int(str[i:i+2])
                if sel[val]:
                    flag = True
                else:
                    sel[val] = True
                    stk.append(i)
                    i += 2
                    
        rlt = 0
        for i, val in enumerate(sel):
            if val == False:
                if rlt == 0:
                    rlt = i
                else:
                    rlt = rlt*10 + i
                    break
        return rlt
            
        
                    
                    
        
        