#User function Template for python3
class Solution:
	def minPoints(self, M, N, points):
		# code here
		dp=[[0 for _ in range(N)]for _ in range(M)]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if i==M-1 and j==N-1:dp[i][j]=max(1-points[i][j],1)
                elif i==M-1:dp[i][j]=max(dp[i][j+1]-points[i][j],1)
                elif j==N-1:dp[i][j]=max(dp[i+1][j]-points[i][j],1)
                else:dp[i][j]=max(min(dp[i+1][j]-points[i][j],dp[i][j+1]-points[i][j]),1)
        return dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		points = []
		for _ in range(m):
			temp = [int(x) for x in input().split()]
			points.append(temp)
		ob = Solution()
		ans = ob.minPoints(m,n,points)
		print(ans)




# } Driver Code Ends