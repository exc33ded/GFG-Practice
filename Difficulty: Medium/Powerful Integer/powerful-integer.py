class Solution:
    def powerfulInteger(self, intervals, k):
        freq={}
        for item in intervals:
            freq[item[0]]=freq.get(item[0],0)+1
            freq[item[1]+1]=freq.get(item[1]+1,0)-1
        freq=list(freq.items())
        freq.sort()
        ans=-1
        count=0
        for item in freq:
            if count>=k:
                ans=item[0]-1
            count+=item[1]
        return ans
            
