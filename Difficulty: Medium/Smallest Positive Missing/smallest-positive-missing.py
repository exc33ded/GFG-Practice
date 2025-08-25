class Solution:
    def missingNumber(self, arr):
        # code here
        s = set(arr)
        
        num = 1
        
        while True:
            if num not in s:
                return num
            num += 1
                
        
        