"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        str = self.travel(root)
        return str

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        data = data.split(',')
        root, data = self.untravel(data)
        return root
        
    def travel(self, root):
        s = ''
        if root == None:
            return '#,'
        s += str(root.val) + ','
        s += self.travel(root.left)
        s += self.travel(root.right)
        return s
        
    def untravel(self, data):
        if data[0] == '#':
            return None, data[1:]
        root = TreeNode(int(data[0]))
        root.left, data = self.untravel(data[1:])
        root.right, data = self.untravel(data)
        return root, data
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        