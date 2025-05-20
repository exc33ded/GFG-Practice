class Solution(object):
    def kthSmallest(self, m, n, k):
        #code here
        lo,hi = 0,m*n+1
        while lo<hi:
            mid = (lo+hi)//2
            val = 0
            for i in range(m):
                val+=min(n,(mid//(i+1)))
            if val>=k:
                hi = mid
            else:
                lo = mid+1
        return hi