#User function Template for python3

class Solution:
    def largestSubsquare(self, n, A):
        #code here
        ROWS,COLS = len(A),len(A[0])
        dp = [[[0,0] for i in range(ROWS+1)] for j in range(COLS+1)]
        
        for i in range(ROWS):
            for j in range(COLS):
                if A[i][j] == 'X':
                    dp[i+1][j+1][0] = dp[i][j+1][0] + 1
                    dp[i+1][j+1][1] = dp[i+1][j][1] + 1
                    
                    
        maxi = 0
        
        for i in range(ROWS,0,-1):
            for j in range(COLS,0,-1):
                curMin = min(dp[i][j][0],dp[i][j][1])
                while curMin > maxi:
                    if dp[i-curMin+1][j][1] >= curMin and dp[i][j-curMin+1][0] >= curMin:
                        maxi = curMin
                        
                    else:
                        curMin -= 1
                        
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(n,a))
# } Driver Code Ends