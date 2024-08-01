class Solution:
	def editDistance(self, s, t):
		# Code here
		n = len(s)
        m = len(t)
        
        dp = [0] * (m+1)
        
        for j in range(m+1):
            dp[j] = j
        
        for i in range(1, n+1):
            prev = dp[0]  # Store the value of dp[i-1][0]
            dp[0] = i     # Update dp[i][0]
            for j in range(1, m+1):
                temp = dp[j]  # Store the value of dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[j] = prev  # Update dp[i][j] using dp[i-1][j-1]
                else:
                    dp[j] = 1 + min(prev, dp[j-1], dp[j])  # Update dp[i][j] using the minimum of the surrounding cells
                prev = temp  # Update prev for the next iteration
         
        return dp[-1]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends