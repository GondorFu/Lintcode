class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        import ctypes
        a = ctypes.c_int32(a).value
        a = ctypes.c_int32(a).value
        while b != 0:
            carry = ctypes.c_int32(a & b).value
            a = ctypes.c_int32(a ^ b).value
            b = ctypes.c_int32(carry << 1).value

        return a