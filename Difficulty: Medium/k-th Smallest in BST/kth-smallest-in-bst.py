#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        val=[0]

        ret=[-1]

        def fun(root,k):

            if root==None:

                return

            fun(root.left,k)

            val[0]+=1

            if val[0]==k:

                ret[0]=root.data

            fun(root.right,k)

            return

        fun(root,k)

        return ret[0]
