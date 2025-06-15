from math import ceil
class Solution:
    def smallestDivisor(self, arr, k):
        def check(t):
            res=0
            for i in arr:
                res+=ceil(i/t)
            return res
            
        low=1
        high=max(arr)
        res=-1
        while(low<=high):
            mid=(low+high)//2
            if check(mid)>k:
                low=mid+1
            else:
                res=mid
                high=mid-1
        return res