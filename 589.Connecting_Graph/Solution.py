class ConnectingGraph:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.index = [i for i in range(0, n+1)]
        
    def __find_index(self, a):
        if self.index[a] != a:
            self.index[a] = self.__find_index(self.index[a])
        return self.index[a]


    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        i = self.__find_index(a)
        j = self.__find_index(b)
        if i < j:
            self.index[j] = i
        else:
            self.index[i] = j
        
        


    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        # Write your code here
        if self.__find_index(a) == self.__find_index(b):
            return True
        else:
            return False
