#User function Template for python3

class Solution:
    def printDiamond(self, n):
        # Code here
        
        for i in range(1, n+1):
            
            print(" "*(n - i), end = "")
            print("* "*i)
            
        
        for i in range(n+1, 2*n+1):
            
            i = 2*n + 1 - i
            
            print(" "*(n - i), end = "")
            print("* "*i)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends