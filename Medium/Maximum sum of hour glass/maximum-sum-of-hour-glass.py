#User function Template for python3

class Solution:
    def findMaxSum(self,rows,cols,grid):
        if N < 3 or M < 3:
            return -1
            
        gridsum = lambda r,c : sum(grid[r - 1][c - 1: c + 2]) + grid[r][c] + sum(grid[r + 1][c - 1: c + 2])
        
        return max(gridsum(r, c) for r in range(1, rows - 1) for c in range(1, cols - 1))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends