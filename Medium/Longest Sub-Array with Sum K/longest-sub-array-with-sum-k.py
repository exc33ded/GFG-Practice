#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        hm = {0: -1}
        long_len = 0
        cum_sum = 0
        
        for i in range(n):
            cum_sum += arr[i]

            if (cum_sum - k) in hm:
                long_len = max(long_len, i - hm[cum_sum - k])
                
            if cum_sum not in hm:
                hm[cum_sum] = i
        
        return long_len
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends