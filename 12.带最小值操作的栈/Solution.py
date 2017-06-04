class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.data = list()
        self.dataM = list()

    def push(self, number):
        # write yout code here
        if len(self.data) == 0 or number <= self.dataM[-1]:
            self.dataM.append(number)
        else:
            self.dataM.append(self.dataM[-1])
        self.data.append(number)
            

    def pop(self):
        # pop and return the top item in stack
        self.dataM.pop()
        return self.data.pop()

    def min(self):
        # return the minimum number in stack
        return self.dataM[-1]