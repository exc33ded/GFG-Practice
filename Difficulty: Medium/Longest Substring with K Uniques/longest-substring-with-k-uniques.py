from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        
        s = list(s)
        freq = defaultdict(int)
        maxx , l = -1 , 0
        
        for r in range(len(s)):
            
            freq[s[r]] += 1
            
            while len(freq) > k:
                
                freq[s[l]] -= 1
                
                
                if freq[s[l]] == 0: del freq[s[l]]
                
                l += 1
            
            if len(freq) == k: maxx = max(maxx, r - l + 1)
        
        
        return maxx

