'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

class Heap:
    
    def __init__(self, score):
        self.hp = [score]
    
    def insert(self, score):
        i = len(self.hp)
        self.hp.append(score)
        while i != 0 and self.hp[(i-1)//2] <= self.hp[i]:
            self.hp[(i-1)//2], self.hp[i] = self.hp[i], self.hp[(i-1)//2]
            i = (i-1)//2
            
    def pop(self):
        if len(self.hp) == 1:
            return self.hp.pop()
        v = self.hp[0]
        self.hp[0] = self.hp.pop()
        i = 0
        while 2*i+2 < len(self.hp):
            if self.hp[i] <= self.hp[2*i+1] and self.hp[2*i+2] <= self.hp[2*i+1]:
                self.hp[i], self.hp[2*i+1] = self.hp[2*i+1], self.hp[i]
                i = 2*i+1
            elif self.hp[i] <= self.hp[2*i+2] and self.hp[2*i+1] <= self.hp[2*i+2]:
                self.hp[i], self.hp[2*i+2] = self.hp[2*i+2], self.hp[i]
                i = 2*i+2
            else:
                break
        if 2*i+1 < len(self.hp) and self.hp[i] <= self.hp[2*i+1]:
            self.hp[i], self.hp[2*i+1] = self.hp[2*i+1], self.hp[i]
            i = 2*i+1
        return v
        
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        dictHp = {}
        for v in results:
            if v.id in dictHp:
                dictHp[v.id].insert(v.score)
            else:
                dictHp[v.id] = Heap(v.score)
        d = {}       
        for i, v in dictHp.items():
            s = 0
            k = 5
            while k > 0:
                s += v.pop()
                k -= 1
            s /= 5.0
            d[i] = s
                
        return d