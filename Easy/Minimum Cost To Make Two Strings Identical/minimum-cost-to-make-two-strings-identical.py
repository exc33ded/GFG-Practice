#User function Template for python3
class Solution:
	def findMinCost(self, x, y, costX, costY):
		# code here
		m, n = len(X), len(Y)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
    
        for row in range(1, m + 1):
            dp[row][0] = dp[row - 1][0] + costX
        
        for col in range(1, n + 1): 
            dp[0][col] = dp[0][col - 1] + costY
        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    
                else:
                    dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)
        
                   
        return dp[-1][-1]
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, costX, costY = input().split()
        costX = int(costX)
        costY = int(costY)
        ob = Solution()
        ans = ob.findMinCost(X, Y, costX, costY)
        print(ans)

# } Driver Code Ends