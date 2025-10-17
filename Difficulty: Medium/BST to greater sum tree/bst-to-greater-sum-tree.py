'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        # code here
        
        sm=0
        def dfs(cur=root):
            nonlocal sm
            if not cur:
                return 0
            dfs(cur.right)
            cur.data,sm=sm,sm+cur.data
            dfs(cur.left)
        dfs()
        return root
        
