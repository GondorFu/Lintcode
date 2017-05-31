class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if string == None:
            return string
        rlt = length
        for v in string:
            if v == ' ':
                rlt += 2
        i, j = rlt - 1, length - 1
        while i >= 0:
            if string[j] == ' ':
                string[i-2:i+1] = '%20'
                i = i - 3
            else:
                string[i] = string[j]
                i -= 1
            j -= 1
        return rlt