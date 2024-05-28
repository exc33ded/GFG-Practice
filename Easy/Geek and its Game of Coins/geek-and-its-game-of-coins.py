
class Solution:
    def findWinner(self, N : int, X : int, Y : int) -> int:
        # code here
        dp = [0]*(N+1)
		dp[1]=1
		
		for i in range(2,N+1):
		    
		    if i-1>=0 and not dp[i-1]:
		        dp[i]=1
		        
		    elif i-X>=0 and not dp[i-X]:
		        dp[i]=1  
		        
		    elif i-Y>=0 and not dp[i-Y]:
		        dp[i]=1
	    
	    return dp[-1]	



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        obj = Solution()
        res = obj.findWinner(n, x, y)

        print(res)

# } Driver Code Ends