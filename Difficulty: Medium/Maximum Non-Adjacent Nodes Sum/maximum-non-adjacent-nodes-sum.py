'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        #code here
        def help(root):
            if not root:
                return [0, 0]
            l = help(root.left)
            r = help(root.right)
            include = root.data + l[1] + r[1]
            exclude = max(l) + max(r)
            return [include, exclude]
        res = help(root)
        return max(res)