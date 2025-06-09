from collections import Counter
class Solution:
    def countStrings(self, S): 
        #code here
        
        cnt = Counter(S)
        
        ln = len(S)
        
        ans = sum(c*(c-1)//2 for c in cnt.values())
        
        
        res = ln*(ln-1)//2 - ans
        
        
        res += ans !=0
        
        return res