#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr)
        arr.sort()
        
        res = arr[-1] - arr[0]
        
        for i in range(1, n):
            if arr[i] >= k:
                max_val = max(arr[i-1] + k, arr[-1] - k)
                min_val = min(arr[0] + k, arr[i] - k)
                res = min(res, max_val - min_val)
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends