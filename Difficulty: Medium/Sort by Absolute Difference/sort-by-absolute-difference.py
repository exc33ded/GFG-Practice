class Solution:
    def rearrange(self, arr, x):
        # code here
        return arr.sort(key = lambda k : abs(k-x))
        
        