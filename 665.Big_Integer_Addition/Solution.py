class Solution:
    # @param {string} num1 a non-negative integers
    # @param {string} num2 a non-negative integers
    # @return {string} return sum of num1 and num2
    def addStrings(self, num1, num2):
        # Write your code here
        ctoi = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        itoc = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
        n1, n2 = len(num1), len(num2)
        i, j = n1-1, n2-1
        c = 0
        rlt = ''
        while i >= 0 and j >= 0:
            s = ctoi[num1[i]] + ctoi[num2[j]] + c
            c = 0
            if s >= 10:
                c = 1
                s = s % 10
            rlt += itoc[s]
            i -= 1
            j -= 1
        while i >= 0:
            s = ctoi[num1[i]]+ c
            c = 0
            if s >= 10:
                c = 1
                s = s % 10
            rlt += itoc[s]
            i -= 1
        while j >= 0:
            s = ctoi[num2[j]] + c
            c = 0
            if s >= 10:
                c = 1
                s = s % 10
            rlt += itoc[s]
            j -= 1
            
        if c == 1:
            rlt += '1'
        return rlt[::-1]