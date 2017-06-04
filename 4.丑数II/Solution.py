class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        l = [1]
        m2, m3, m5 = [2], [3], [5]
        i2, i3, i5 = 0, 0, 0
        while len(l) < n:
            if m2[i2] < m3[i3] and m2[i2] < m5[i5]:
                l.append(m2[i2])
                m2.append(l[-1]*2)
                m3.append(l[-1]*3)
                m5.append(l[-1]*5)
                i2 += 1
            elif m2[i2] > m3[i3] and m3[i3] < m5[i5]:
                l.append(m3[i3])
                m3.append(l[-1]*3)
                m5.append(l[-1]*5)
                i3 += 1
            else:
                l.append(m5[i5])
                m5.append(l[-1]*5)
                i5 += 1
            
        return l[-1]

