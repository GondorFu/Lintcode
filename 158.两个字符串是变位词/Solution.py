class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        n = len(s)
        if len(t) != n:
            return False
        d = {}
        for v in s:
            if d.get(v, -1) == -1:
                d[v] = 1
            else:
                d[v] += 1
        for v in t:
            if d.get(v, -1) == -1:
                return False
            d[v] -= 1
            if d[v] < 0:
                return False
        return True
        