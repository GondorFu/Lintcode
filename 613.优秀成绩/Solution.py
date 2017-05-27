class Heap:
    def __init__(self, points, origin):
        self.hp = []
        self.og = origin
        for i, v in enumerate(points):
            self.hp.append(v)
            while i != 0 and self.order(self.hp[(i-1)//2], self.hp[i]):
                self.hp[(i-1)//2], self.hp[i] = self.hp[i], self.hp[(i-1)//2]
                i = (i-1)//2
    
    def pop(self):
        v = self.hp[0]
        if len(self.hp) == 1:
            return v
        self.hp[0] = self.hp.pop()
        i = 0
        while 2*i+2 < len(self.hp):
            if self.order(self.hp[i], self.hp[2*i+1]) and self.order(self.hp[2*i+2], self.hp[2*i+1]):
                self.hp[i], self.hp[2*i+1] = self.hp[2*i+1], self.hp[i]
                i = 2*i+1
            elif self.order(self.hp[i], self.hp[2*i+2]) and self.order(self.hp[2*i+1], self.hp[2*i+2]):
                self.hp[i], self.hp[2*i+2] = self.hp[2*i+2], self.hp[i]
                i = 2*i+2
            else:
                break
        if 2*i+2 == len(self.hp) and self.order(self.hp[i], self.hp[2*i+1]):
            self.hp[i], self.hp[2*i+1] = self.hp[2*i+1], self.hp[i]
        return v

    def order(self, pt1, pt2):
        dis1 = ((pt1.x-self.og.x)**2 + (pt1.y-self.og.y)**2)**0.5
        dis2 = ((pt2.x-self.og.x)**2 + (pt2.y-self.og.y)**2)**0.5
        if dis1 > dis2 or (dis1 == dis2 and (pt1.x > pt2.x or (pt1.x == pt2.x and pt1.y >= pt2.y))):
            return True
        return False

class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        hp = Heap(points, origin)
        rlt = []
        while k > 0:
            rlt.append(hp.pop())
            k -= 1
        return rlt