class Solution:
    def maximizeMedian(self, arr, k):
        n = len(arr)
        arr.sort()
        median = arr[n//2] if n%2!=0 else (arr[n//2]+arr[(n//2)-1])//2
        l = median
        h = median + k
        
        def boolean(arr,mid,k):
            if n%2 != 0:
                for  i in range(n//2,n):
                    if arr[i]<=mid:
                        k -= (mid-arr[i])
                        if k<0:
                            return False
            else:
                k -= (mid-arr[n//2])
                k -= (mid-arr[(n//2)-1])
                if k<0:
                    return False
                for  i in range((n//2)+1,n):
                    if arr[i]<=mid:
                        k -= (mid-arr[i])
                        if k<0:
                            return False 
            return k>=0
        
        while l<=h:
            mid = (l+h)//2
            
            if boolean(arr,mid,k):
                l = mid+1
            else:
                h = mid-1
        
        return h
        
