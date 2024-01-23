#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        res = arr[n-1] - arr[0]
        big = arr[n-1] - k
        small = arr[0] + k
        mini, maxi = 0, 0
        
        for i in range(1, n):
            mini = min(small, arr[i] - k)
            maxi = max(big, arr[i-1] + k)
            
            if mini < 0:
                continue
            res = min(res, maxi - mini)
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends