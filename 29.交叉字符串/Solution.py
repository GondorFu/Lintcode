class Solution:
    """
    @param: : A string
    @param: : A string
    @param: : A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # write your code here
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        if n1 == 0 or n2 == 0:
            rlt = s1 + s2
            for i in range(n3):
                if s3[i] != rlt[i]:
                    return False
            return True
        
        l = [True] + [False for i in range(n1)]
        flag = True
        for i in range(n2+1):
            if not flag:
                break
            flag = False
            for j in range(n1+1):
                if i+j == 0:
                    continue
                elif i != 0 and l[j] and s3[i+j-1] == s2[i-1]:
                    l[j] = True
                    flag = True
                elif j != 0  and l[j-1] and s3[i+j-1] == s1[j-1]:
                    l[j] = True
                    flag = True
                else:
                    l[j] = False
        return l[-1]
                
            
        