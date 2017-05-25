# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point} l1 top-left coordinate of first rectangle
    # @param {Point} r1 bottom-right coordinate of first rectangle
    # @param {Point} l2 top-left coordinate of second rectangle
    # @param {Point} r2 bottom-right coordinate of second rectangle
    # @return {boolean} true if they are overlap or false
    def doOverlap(self, l1, r1, l2, r2):
        # Write your code here
        if l2.x > r1.x or r2.y > l1.y or r2.x < l1.x or l2.y < r1.y:
            return False
        return True