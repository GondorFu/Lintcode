class Solution:
    # @return: The same instance of this class every time
    instance = None
    
    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Solution()
        return cls.instance
        