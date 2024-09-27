#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)
        dp = [float('inf')] * n  # Initialize the DP array with infinity
        dp[0] = 0  # Cost to reach the first stone is 0
        
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                dp[j] = min(dp[j], dp[i] + abs(arr[i] - arr[j]))
        
        return dp[-1] 

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends